from config import parse_args
from transformers import AutoModel
from transformers import AutoTokenizer
from peft import PeftModel
import torch


if __name__ == "__main__":
    args = parse_args()
    model = AutoModel.from_pretrained(args.MODEL_NAME, trust_remote_code=True,device_map='auto')
    tokenizer = AutoTokenizer.from_pretrained(args.MODEL_NAME, trust_remote_code=True)
    model = PeftModel.from_pretrained(model, args.LORA_CHECKPOINT_DIR)

    with torch.no_grad():

        while True:
            text = input("请输入:")
            res, history = model.chat(tokenizer=tokenizer, query=text,max_length=args.CUTOFF_LEN)
            print(res)
            