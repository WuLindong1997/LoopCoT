from config import parse_args
from peft import LoraConfig, get_peft_model
from transformers import AutoTokenizer, AutoModel
import transformers
import torch
import random
from datasets import load_dataset
import os
from transformers import Trainer, TrainingArguments
from typing import Optional

#重写保存checkpoint的方法
# class MyTrainer(Trainer):
#     def _save(self, output_dir: Optional[str] = None, state_dict=None):
#         # If we are executing this function, we are the process zero, so we don't check for that.
#         output_dir = output_dir if output_dir is not None else self.args.output_dir
#         os.makedirs(output_dir, exist_ok=True)
#         def save_tunable_parameters(model, path):
#             saved_params = {
#                 k: v.to("cpu") for k, v in model.named_parameters() if v.requires_grad
#             }
#             # saved_params = model.state_dict()
#             torch.save(saved_params, path)

#         save_tunable_parameters(
#             self.model, os.path.join(output_dir, "chatglm-lora.pt")
#         )

#load lora config
def get_lora_config(args):
    config = LoraConfig(
        r=args.LORA_R,
        lora_alpha=args.LORA_ALPHA,
        lora_dropout=args.LORA_DROPOUT,
        bias='none',
        task_type='CAUSAL_LM',
    )
    return config

#load model and tokenizer
def get_model_and_tokenizer(model_name, config):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_name, trust_remote_code=True).half().cuda()
    model = get_peft_model(model,config)
    return model, tokenizer

def get_masks_and_position_ids(seq, seq_len, context_length, device, gmask=False, position_encoding_2d=True):
    mask_position = (seq_len - 2)  # is equal to `seq.index(mask_token)` or `seq.index(150001)`
    attention_mask = torch.ones((1, context_length, context_length), device=device)
    attention_mask.tril_()
    #attention_mask[..., : mask_position - 1] = 1 和 attention_mask[:,:, : mask_position - 1] = 1 是相等的
    attention_mask[..., : mask_position - 1] = 1
    attention_mask = (attention_mask < 0.5).bool()

    if position_encoding_2d:
        seq_length = seq_len - 1  # is equal to `seq_length = seq.index(150004)`
        position_ids = torch.arange(context_length, dtype=torch.long, device=device)
        if not gmask:
            position_ids[seq_length:] = mask_position
        block_position_ids = torch.cat(
            (
                torch.zeros(seq_length, dtype=torch.long, device=device),
                torch.arange(context_length - seq_length, dtype=torch.long, device=device) + 1,
            )
        )
        position_ids = torch.stack((position_ids, block_position_ids), dim=0)
    else:
        position_ids = torch.arange(context_length, dtype=torch.long, device=device)
        if not gmask:
            position_ids[context_length - 1 :] = mask_position
    return attention_mask, position_ids

#data process dataloader
def data_collator(features: list) -> dict:
    len_ids = [len(feature["input_ids"]) for feature in features]
    longest = max(len_ids) + 1
    input_ids = []
    # attention_mask_list = []
    # position_ids_list = []
    labels_list = []

    #lambda是从大到小进行排一下顺序
    for ids_l, feature in sorted(zip(len_ids, features), key=lambda x: -x[0]):
        ids = feature["input_ids"]
        seq_len = feature["seq_len"]

        #label只需要后面生成的，前面的prompt都用-100代替
        labels = (
            [-100] * (seq_len - 1)
            + ids[(seq_len - 1) :]
            + [tokenizer.eos_token_id]
            + [-100] * (longest - ids_l - 1)
        )
        #以最长的作为标准，短的运用eop_token_id进行填充
        ids = ids + [tokenizer.eos_token_id] * (longest - ids_l)
        _ids = torch.LongTensor(ids)

        # 这里添加添加mask
        # attention_mask, position_ids = get_masks_and_position_ids(
        #     ids, seq_len, longest, _ids.device, gmask=False
        # )
        # attention_mask_list.append(attention_mask)
        # position_ids_list.append(position_ids)

        labels_list.append(torch.LongTensor(labels))
        input_ids.append(_ids)
    input_ids = torch.stack(input_ids)
    labels = torch.stack(labels_list)
    # attention_mask = torch.stack(attention_mask_list)
    # position_ids = torch.stack(position_ids_list)
    return {
        "input_ids": input_ids,
        "labels": labels,
        # "attention_mask": attention_mask,
        # "position_ids": position_ids,
    }

#data process dataset
def preprocess(example):
    
    prompt = example["prompt"]
    target = example["answer"]
    prompt_ids = tokenizer.encode(prompt, max_length=args.CUTOFF_LEN, truncation=True)
    target_ids = tokenizer.encode(target, max_length=args.CUTOFF_LEN, truncation=True, add_special_tokens=False)
    input_ids = prompt_ids + target_ids + [tokenizer.eos_token_id]
    return {"input_ids": input_ids, "seq_len": len(prompt_ids)}

#load trainer
def get_trainer(args, model, data):
    GRADIENT_ACCUMULATION_STEPS = args.BATCH_SIZE // args.MICRO_BATCH_SIZE
    trainer = Trainer(
        model=model,
        train_dataset=data['train'],
        eval_dataset=data["test"],
        args=TrainingArguments(
            per_device_train_batch_size=args.MICRO_BATCH_SIZE,
            gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
            warmup_steps=args.WARMUP_STEPS,
            num_train_epochs=args.EPOCHS,
            learning_rate=args.LEARNING_RATE,
            logging_steps=args.LOGGING_STEPS,
            evaluation_strategy="steps",
            eval_steps=args.EVAL_STEPS,
            save_strategy="steps",
            save_steps=args.SAVE_STEPS,
            output_dir=args.OUTPUT_DIR,
            overwrite_output_dir=True,
            save_total_limit=args.SAVE_TOTAL_LIMIT,
            remove_unused_columns=False,
            fp16=True,
        ),
        data_collator=data_collator
    )

    return trainer

#load dataset
def get_dataset(args):
    if args.DATA_TYPE == "json":
        dataset = load_dataset("json", data_files={'train':args.DATA_PATH_TRAIN,'test':args.DATA_PATH_TEST},cache_dir='/root/autodl-tmp/wld/cache')
    elif args.DATA_TYPE == "txt":
        dataset = load_dataset("text", data_files=args.DATA_PATH)

    return dataset



if __name__ == "__main__":
    args = parse_args()

    lora_config = get_lora_config(args)
    model, tokenizer = get_model_and_tokenizer(args.MODEL_NAME, lora_config)

    
    tokenized_datasets = get_dataset(args)


    tokenized_datasets = tokenized_datasets.map(function=preprocess)


    trainer = get_trainer(args, model, tokenized_datasets)
    # trainer.train(resume_from_checkpoint=False)
    trainer.train()
    model.save_pretrained(args.OUTPUT_DIR + "/model_final")
