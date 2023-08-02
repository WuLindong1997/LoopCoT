import json
import argparse
import random
def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--poem_path',type=str,default='/root/autodl-tmp/wld/data/poem_test_info.json')
    arg_parser.add_argument('--type',type=str,choices=['generation','appreciation','mix'],default='generation')
    arg_parser.add_argument('--save_path',type=str,default='/root/autodl-tmp/wld/data/generation/test.json')
    args = arg_parser.parse_args()
    return args


#诗歌生成数据处理
def process_poem_generation():
    with open(args.poem_path,'r',encoding='utf-8')as file:
        all_poem = json.loads(file.read())
    
    result = []
    instruction = "请根据以下提供的信息进行诗歌生成："
    for line in all_poem:
        
        if random.random()>0.5:
            theme = line['keywords']
        else:
            theme = line['chatgpt_appreciation_summary']
        style = line["poem_class"]
        answer = line["poem"]

        line_dict = {"prompt":f"{instruction}\n\n生成主题：{theme}\n格式：{style}\n请生成诗歌：\n","answer":f"{answer}"}
        result.append(line_dict)

    # with open(args.save_generation_path,'w',encoding='utf-8')as file1:
    #     file1.write(json.dumps(result,ensure_ascii=False))
    return result

#诗歌鉴赏数据处理
def process_poem_appreciation():
    with open(args.poem_path,'r',encoding='utf-8')as file:
        all_poem = json.loads(file.read())
    
    result = []
    instruction = '请根据以下诗歌进行鉴赏：'
    for line in all_poem:
        
        poem = line['poem']
        answer = line['chatgpt_appreciation']
        line_dict = {"prompt":f"{instruction}\n\n诗歌：{poem}\n请鉴赏诗歌：\n","answer":f"{answer}"}
        result.append(line_dict)

    # with open(args.save_appreciation_path,'w',encoding='utf-8')as file1:
    #     file1.write(json.dumps(result,ensure_ascii=False))
    return result

def save_data(data):
    with open(args.save_path,'w',encoding='utf-8')as file1:
        file1.write(json.dumps(data,ensure_ascii=False))
        print(f'save path {args.save_path}:over all!')

if __name__ == '__main__':
    args = get_args()

    if args.type == 'generation':
        generation_data = process_poem_generation()
        save_data(generation_data)
    elif args.type == 'appreciation':
        appreciation_data = process_poem_appreciation()
        save_data(appreciation_data)
    else:
        generation_data = process_poem_generation()
        appreciation_data = process_poem_appreciation()
        generation_data.extend(appreciation_data)
        save_data(generation_data)