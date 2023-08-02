from config import parse_args
from transformers import AutoModel
from transformers import AutoTokenizer
from peft import PeftModel
import torch
import json
from tqdm import tqdm
import jieba
import os
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge_chinese import Rouge
import numpy as np

def get_data(args):
    with open(args.DATA_PATH_TEST,'r',encoding='utf-8')as file:
        json_lines = json.loads(file.read())
    return json_lines[:]

def computer_scores(test_data,peft_model):
    generation_result = []
    for line in tqdm(test_data,desc='generation res:'):
        with torch.no_grad():
            reference = line['prompt']
            res, _ = peft_model.chat(tokenizer=tokenizer, query=reference,max_length=args.CUTOFF_LEN)
            line['res'] = res
            generation_result.append(line)
    score_dict = {
            "rouge-1": [],
            "rouge-2": [],
            "rouge-l": [],
            "bleu-4": []
        }
    for line in generation_result:
        pred = line['res']
        label = line['answer']
        hypothesis = list(jieba.cut(pred))
        reference = list(jieba.cut(label))
        rouge = Rouge()
        scores = rouge.get_scores(' '.join(hypothesis) , ' '.join(reference))
        result = scores[0]
        
        for k, v in result.items():
            score_dict[k].append(round(v["f"] * 100, 4))
        bleu_score = sentence_bleu([list(label)], list(pred), smoothing_function=SmoothingFunction().method3)
        score_dict["bleu-4"].append(round(bleu_score * 100, 4))
    for k, v in score_dict.items():
        score_dict[k] = float(np.mean(v))
    return score_dict

if __name__ == "__main__":
    args = parse_args()
    scores = []
    model = AutoModel.from_pretrained(args.MODEL_NAME, trust_remote_code=True,device_map='auto')
    
    for file_name in os.listdir(args.LORA_CHECKPOINT_METRIC_DIR):
        if "check" not in file_name:
            continue
        check_point_path = os.path.join(args.LORA_CHECKPOINT_METRIC_DIR,file_name)
        tokenizer = AutoTokenizer.from_pretrained(args.MODEL_NAME, trust_remote_code=True)
        peft_model = PeftModel.from_pretrained(model, check_point_path)

        test_data = get_data(args)

        score = computer_scores(test_data,peft_model)
        score['source_checkpoint'] = check_point_path
        scores.append(score)
        peft_model = ''
    with open(args.SAVE_METRIC,'w',encoding='utf-8')as file1:
        file1.write(json.dumps(scores,ensure_ascii=False))

            