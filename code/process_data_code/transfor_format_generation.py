import json
import argparse
import re

def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--data_path',default='/root/autodl-tmp/wld/data/poem_train_all.json',help="data path")
    arg_parser.add_argument('--save_path',default='/root/autodl-tmp/wld/data/poem_train_info.json',help='save path')
    
    return arg_parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    with open(args.data_path,'r',encoding='utf-8')as file:
        json_line= list(map(json.loads,file.readlines()))

    result = []
    for line in json_line:
        match_title = re.match(r'^诗歌题目:(.*?)，',line['prompt'])
        match_keywords = re.findall(r'主题信息:(.*)',line['prompt'])
        title = match_title.group(1)
        if len(title) >= 9:
            continue
        keywords = match_keywords[0]
        size = 0 
        for i in re.split(r'[,.。、！？?!，\s]',line['answer']):
            size+=len(i)
        size_len = size//len(re.split(r'[,.。、！？?!，\s]',line['answer']))
        if size_len == 5:
            if len(re.split(r'[,.。、！？?!，\s]',line['answer']))<=4:
                theme = '5言绝句'
            else:
                theme = '5言律诗'
        elif size_len == 7:
            if len(re.split(r'[,.。、！？?!，\s]',line['answer']))<=4:
                theme = '7言绝句'
            else:
                theme = '7言律诗'
        else:
            theme = '词'

        poem_info = {
            "title":title,
            "keywords":keywords,
            "poem_class":theme,
            "poem":line['answer'],
            "chatgpt_appreciation":line['chatgpt'].replace('主题大意：',''),
            "chatgpt_appreciation_summary":line['chatgpt_text_abstract']
        }
        result.append(poem_info)

    with open(args.save_path,'w',encoding='utf-8')as file_w:
        file_w.write(json.dumps(result,ensure_ascii=False))
