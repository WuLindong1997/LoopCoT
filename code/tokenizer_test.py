from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b',trust_remote_code=True)

pass
tokenizer.train_new_from_iterator
