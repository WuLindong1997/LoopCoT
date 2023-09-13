#!/bin/bash
# export CUDA_VISIBLE_DEVICES=1 
CUDA_VISIBLE_DEVICES=1 python chatglm_train_lora.py \
	--MICRO_BATCH_SIZE 6\
	--BATCH_SIZE 36 \
	--EPOCHS 30 \
	--LEARNING_RATE 2e-5 \
	--CUTOFF_LEN 1024 \
	--LORA_R 16 \
	--MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
	--OUTPUT_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_single_chatglm \
	--DATA_PATH_TRAIN /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/train.json \
	--DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/test.json \
	--DATA_PATH_CACHE /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/cache \
	--DATA_TYPE json \
	--SAVE_STEPS 100 \
    --EVAL_STEPS 100 \
	
rm -rf /mnt/vepfs/lingxin/Pretrain-data/wulindong/cache/*

CUDA_VISIBLE_DEVICES=1 python chatglm_train_lora.py \
	--MICRO_BATCH_SIZE 6\
	--BATCH_SIZE 36 \
	--EPOCHS 30 \
	--LEARNING_RATE 2e-5 \
	--CUTOFF_LEN 1024 \
	--LORA_R 16 \
	--MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
	--OUTPUT_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_mix_all_chatglm \
	--DATA_PATH_TRAIN /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/mix_story_all/train.json \
	--DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/mix_story_all/test.json \
	--DATA_PATH_CACHE /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/cache \
	--DATA_TYPE json \
	--SAVE_STEPS 100 \
    --EVAL_STEPS 100 \

rm -rf /mnt/vepfs/lingxin/Pretrain-data/wulindong/cache/*

CUDA_VISIBLE_DEVICES=1 python chatglm_train_lora.py \
	--MICRO_BATCH_SIZE 6\
	--BATCH_SIZE 36 \
	--EPOCHS 30 \
	--LEARNING_RATE 2e-5 \
	--CUTOFF_LEN 1024 \
	--LORA_R 16 \
	--MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
	--OUTPUT_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_mix_half_chatglm \
	--DATA_PATH_TRAIN /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/mix_story_half/train.json \
	--DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/mix_story_half/test.json \
	--DATA_PATH_CACHE /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/cache \
	--DATA_TYPE json \
	--SAVE_STEPS 100 \
    --EVAL_STEPS 100 \

rm -rf /mnt/vepfs/lingxin/Pretrain-data/wulindong/cache/*
