
# mix all
python model_evaluation_best_ckpt_mean.py \
            --CUTOFF_LEN 1024 \
            --MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_mix_all_chatglm \
            --SAVE_METRIC /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/evaluation_result/story_mix_all_final_result.json \
            --DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/test.json \
            --CKPT  checkpoint-300\

# mix half          
python model_evaluation_best_ckpt_mean.py \
            --CUTOFF_LEN 1024 \
            --MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_mix_half_chatglm \
            --SAVE_METRIC /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/evaluation_result/story_mix_half_final_result.json \
            --DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/test.json \
            --CKPT  checkpoint-300\

# single
python model_evaluation_best_ckpt_mean.py \
            --CUTOFF_LEN 1024 \
            --MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_single_chatglm \
            --SAVE_METRIC /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/evaluation_result/story_single_final_result.json \
            --DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/test.json \
            --CKPT  checkpoint-300\


