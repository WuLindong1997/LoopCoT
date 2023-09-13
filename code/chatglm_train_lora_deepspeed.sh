#!/bin/bash
# CUDA_VISIBLE_DEVICES='0'
deepspeed \
	--include localhost:0,1 chatglm_train_lora.py \
	--MICRO_BATCH_SIZE 4\
	--BATCH_SIZE 16 \
	--EPOCHS 30 \
	--LEARNING_RATE 2e-5 \
	--CUTOFF_LEN 256 \
	--LORA_R 16 \
	--MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
	--OUTPUT_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_single_chatglm \
	--DATA_PATH_TRAIN /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/generation/train.json \
	--DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/generation/test.json \
	--DATA_PATH_CACHE /mnt/vepfs/lingxin/pip Pretrain-data/wulindong/LoopCoT/cache \
	--DATA_TYPE json \
	--SAVE_STEPS 100 \
    --EVAL_STEPS 10 \

