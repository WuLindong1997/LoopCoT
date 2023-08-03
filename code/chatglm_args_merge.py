from transformers import AutoTokenizer,AutoModel
import torch
from config import parse_args
from peft import PeftModel

if __name__ == "__main__":
    args = parse_args()

    model = AutoModel.from_pretrained("/root/autodl-tmp/wld/model/chatglm2-6b", trust_remote_code=True).half().cuda()
    
    peft_path1 = "/root/autodl-tmp/wld/model/lora_check_point/mix_data_chatglm/checkpoint-9000/adapter_model.bin"
    peft_path2 = "/root/autodl-tmp/wld/model/lora_check_point/mix_data_chatglm/checkpoint-10000/adapter_model.bin"
    state_dict1 = torch.load(peft_path1, map_location="cuda")
    state_dict2 = torch.load(peft_path2, map_location="cuda")
    for key in state_dict2.keys():
            state_dict2[key] = (state_dict2[key]+state_dict1[key])/2.0
            # state_dict2[key] = state_dict1[key]
    torch.save(state_dict2,'/root/autodl-tmp/wld/model/merge_model/adapter_model.bin')
    model = PeftModel.from_pretrained(model,'/root/autodl-tmp/wld/model/merge_model')

    tokenizer = AutoTokenizer.from_pretrained(args.MODEL_NAME, trust_remote_code=True)
    with torch.no_grad():
        while True:
            text = input("请输入:")
            res, history = model.chat(tokenizer=tokenizer, query=text,max_length=args.CUTOFF_LEN)
            print(res)

 
            