import json


with open('/root/autodl-tmp/wld/data/appreciation_info.json','r',encoding='utf-8')as file:
    data1 = json.loads(file.read())

with open('/root/autodl-tmp/wld/data/poem_train_info.json','r',encoding='utf-8')as file1:
    data2 = json.loads(file1.read())

data1.extend(data2)

with open("/root/autodl-tmp/wld/data/train_data.json",'w',encoding='utf-8')as file2:
    file2.write(json.dumps(data1,ensure_ascii=False))
