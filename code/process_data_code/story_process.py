import json
import random

random.seed(10)

def get_data(path):
    with open(path,'r',encoding="utf-8")as file:
        all_data = json.loads(file.read())
    return all_data


if __name__ == "__main__":

    path = "/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_raw.json"
    data = get_data(path)
    random.shuffle(data)
    
    test_size = len(data)//10
    train_data = data[test_size:]
    test_data = data[:test_size]
    
    with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/code/process_data_code/instruction_story_generation.txt",'r',encoding="utf-8")as file:
        instruction_story_generation = file.read().split('\n')
    with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/code/process_data_code/instruction_story_summarize.txt",'r',encoding="utf-8")as file:
        instruction_story_summarize = file.read().split('\n')
        
    story_generation_train = []
    story_generation_test = []
    story_summarize_train = []
    story_summarize_test = []

    for i in train_data:
        prompt = random.sample(instruction_story_generation,k = 1)[0] + '\n\n' + i["keywords"]
        answer = i["story"]
        story_generation_train.append({"prompt":prompt,"answer":answer})
    
    for i in test_data:
        prompt = random.sample(instruction_story_generation,k = 1)[0] + '\n\n' + i["keywords"]
        answer = i["story"]
        story_generation_test.append({"prompt":prompt,"answer":answer})

    for i in train_data:
        prompt = random.sample(instruction_story_summarize,k = 1)[0] + '\n\n' + i["story"]
        answer = i["keywords"]
        story_summarize_train.append({"prompt":prompt,"answer":answer})
    
    for i in test_data:
        prompt = random.sample(instruction_story_summarize,k = 1)[0] + '\n\n' + i["story"]
        answer = i["keywords"]
        story_summarize_test.append({"prompt":prompt,"answer":answer})

    #==================half and all====================
    # story_generation_train +=  story_summarize_train[:len(story_generation_train)//2]
    # story_generation_train +=  story_summarize_train
    #==================half and all====================
    
    # with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/mix_story_half/train.json",'w',encoding="utf-8")as file:
    #     json.dump(story_generation_train,file,ensure_ascii=False,indent=4)

    # with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/mix_story_half/test.json",'w',encoding="utf-8")as file:
    #     json.dump(story_generation_test,file,ensure_ascii=False,indent=4)
    #==================half and all====================

    with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/train.json",'w',encoding="utf-8")as file:
        json.dump(story_generation_train,file,ensure_ascii=False,indent=4)

    with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/test.json",'w',encoding="utf-8")as file:
        json.dump(story_generation_test,file,ensure_ascii=False,indent=4)

    with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_summarize/train.json",'w',encoding="utf-8")as file:
        json.dump(story_summarize_train,file,ensure_ascii=False,indent=4)

    with open("/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_summarize/test.json",'w',encoding="utf-8")as file:
        json.dump(story_summarize_test,file,ensure_ascii=False,indent=4)
    

    


        

    
