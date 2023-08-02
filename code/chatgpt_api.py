"""
    @Time    : 2023/6/27 15:34
    @Author  : LindongWu
    @Email   : wldsty@126.com
    @File    : chatgpt_api.py
"""
# -*- coding: utf-8 -*-

import sys
import json
import os
import time
import requests
from tqdm import tqdm
import multiprocessing
import argparse
def get_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--dataset_path', type=str,
                             default='/root/autodl-tmp/wld/data')
    args_parser.add_argument('--save_path', type=str,
                             default='/root/autodl-tmp/wld/data/rewrite')
    args_parser.add_argument('--pool_num', type=int, default=10)
    args = args_parser.parse_args()
    return args

def read_jsonl(input_file: str) -> list:
    with open(input_file, 'r', encoding='utf-8') as f:
        # lines = f.readlines()
        lines = json.loads(f.read())
    return lines


def get_answer(line, retry_count=3):
    payload, data = line[0], line[1]

    # 公司的key
    url = "https://api.openai-sb.com/v1/chat/completions"
    headers = {
        # 个人的key
        "Authorization": "Bearer sb-1c9d8211cdbac8c808ba47226b7790f92c348b4e0e4ed2de",

        # 公司的key
        # "Authorization": "Bearer sb-c1846034d6d59562cfb8124f7b383d280db3f249c58bda1d",
        # "Content-Type": "application/json"
    }

    try:
        # 请求访问接口
        time.sleep(1)
        response = requests.post(url, json=payload, headers=headers).json()
        # 取出回复获取答案
        answer = response['choices'][0]['message']['content']
        print("修改前：\t"+payload['messages'][1]['content'])
        print("修改后：\t"+answer)
        print('')

        # 放入在data数据中加入获得的答案字段
        data['chatgpt_apperation_summary'] = answer

    except Exception as e:
        print("发生了异常:", str(e))
        if retry_count > 0:
            print("等待2秒后进行重试...")
            time.sleep(2)
            return get_answer(line, retry_count=retry_count - 1)
        else:
            print("重试次数已达上限，无法获取答案。")
            return None
    if len(data['keywords'].split(' ')) > 5:
        return None
    return data
    # write_to_json(data, save_path)


def write_to_json(data, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')





if __name__ == '__main__':

    args = get_args()
    # 加载数据文件路径
    input_files = []
    output_files = []
    for root, dirs, files in os.walk(args.dataset_path):
        for file in files:
            if file.endswith("appreciation_info.json") and file == 'appreciation_info.json':
                input_files.append(os.path.join(root, file))
                output_files.append(os.path.join(args.save_path, file))

    for file_path, save_path in zip(input_files, output_files):
        # 读取文件,将数据转化为prompt
        datas = read_jsonl(file_path)
        payloads = []
        
        for data in tqdm(datas):
            #关键字生成的system massage
            # system_massage = f"You are an assistant who is good at summarizing keywords. Given a poem, you can summarize 1 keyword based on the meaning of each poem, and no more than 5 keywords can be generated in total."
            #summary的system massage
            system_massage = f"You are characterized as an assistant who is good at summarizing a paragraph, and your summary is very short."
            
            prompt = f"下面是一段话，请对这段话进行总结，保证总结的句子非常简短。严格要求总结为13个字之内（可以放弃前面一部分信息，或者放弃后面一部分信息）。\n\n{data['chatgpt_appreciation']}"
            payload = {
                "model": "gpt-3.5-turbo-0613",
                "stream": False,
                "top_p": 0.95,
                "temperature": 1,
                "messages": [
                    {"role": "system", "content": system_massage},
                    {"role": "user", "content": prompt},
                ]
            }
            # 可以修改prompt
            payloads.append([payload, data])



        # 整理好的数据放入接口进行处理
        # 多线程
        # lock = multiprocessing.Lock()
        # with ThreadPoolExecutor(max_workers=8) as executor:
        #     for payload in tqdm(payloads):
        #         executor.submit(get_answer, *payload)

        # 多进程
        # lock = multiprocessing.Lock()
        with multiprocessing.Pool(args.pool_num) as pool:
            result = list(pool.map(get_answer, payloads))
        result = [i for i in result if i!= None]
        
        with open(save_path,'w',encoding='utf-8') as file_w:
            file_w.write(json.dumps(result,ensure_ascii=False))

