from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("/root/autodl-tmp/wld/model/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("/root/autodl-tmp/wld/model/chatglm2-6b", trust_remote_code=True).half().cuda()
model = model.eval()
history =  []
while True:
    text = input("请输入：")
    response, his = model.chat(tokenizer, text, history)
    history = his
    print('Chatbot：'+response)
