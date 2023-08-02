import json
import argparse
import re

def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--data_path',default='/root/autodl-tmp/wld/data/appreciation_prompt_train.json',help="data path")
    arg_parser.add_argument('--save_path',default='/root/autodl-tmp/wld/data/appreciation_train_info.json',help='save path')
    
    return arg_parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    with open(args.data_path,'r',encoding='utf-8')as file:
        json_line= list(map(json.loads,file.readlines()))

    result = []
    for line in json_line:
        title = line['prompt'].split("\n")[1].replace('题目：','')
        poem = re.findall(r'诗句:(.*)',line['prompt'],re.DOTALL )[0].replace('\n','').strip(' ').replace(' ','')
        if len(title) >= 9:
            continue
        keywords = ''
        size = 0 
        for i in re.split(r'[,.。、！？?!，\s]',poem):
            size+=len(i)
        size_len = size//(len(re.split(r'[,.。、！？?!，\s]',poem))-1)
        if size_len == 5:
            if len(re.split(r'[,.。、！？?!，\s]',poem))-1<=4:
                theme = '5言绝句'
            else:
                theme = '5言律诗'
        elif size_len ==7:
            if len(re.split(r'[,.。、！？?!，\s]',poem))-1<=4:
                theme = '7言绝句'
            else:
                theme = '7言律诗'
        else:
            theme = '词'

        poem_info = {
            "title":title,
            "keywords":keywords,
            "poem_class":theme,
            "poem":poem,
            "chatgpt_appreciation":line['answer'],
            "chatgpt_apperation_summary":''
        }
        result.append(poem_info)

    with open(args.save_path,'w',encoding='utf-8')as file_w:
        file_w.write(json.dumps(result,ensure_ascii=False))
