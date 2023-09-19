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
        print(data)
        print(answer)
        print('_______________')

        # 放入在data数据中加入获得的答案字段
        

    except Exception as e:
        print("发生了异常:", str(e))
        if retry_count > 0:
            print("等待2秒后进行重试...")
            time.sleep(2)
            return get_answer(line, retry_count=retry_count - 1)
        else:
            print("重试次数已达上限，无法获取答案。")
            return None
    
    return data
    # write_to_json(data, save_path)


def write_to_json(data, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')





if __name__ == '__main__':

    with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/code/ok12.txt",'r',encoding="utf-8")as file:
        datas = file.read().split('\n')
    payloads = []
    
    for data in tqdm(datas):
        #关键字生成的system massage
        # system_massage = f"You are an assistant who is good at summarizing keywords. Given a poem, you can summarize 1 keyword based on the meaning of each poem, and no more than 5 keywords can be generated in total."
        #summary的system massage
        
        payload = {
            "model": "gpt-3.5-turbo-0613",
            "stream": False,
            "top_p": 0.95,
            "temperature": 1,
            "messages": [
                {"role": "user", "content": data},
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
    # for i in payloads:
    with multiprocessing.Pool(20) as pool:
        a = list(pool.imap(get_answer,payloads))
        # get_answer(i)
    
    
    

