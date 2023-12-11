# python model_evaluation.py \
#             --CUTOFF_LEN 256 \
#             --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
#             --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
#             --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/single_data_appreciation_evaluation.json \
#             --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_appreciation.json \
            
# python model_evaluation.py \
#             --CUTOFF_LEN 256 \
#             --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
#             --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/generation_poem_chatglm2 \
#             --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/single_data_generation_evaluation.json \
#             --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_generation.json \

# CUDA_VISIBLE_DEVICES=1 python model_evaluation.py \
#             --CUTOFF_LEN 1024 \
#             --MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
#             --LORA_CHECKPOINT_METRIC_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_single_chatglm \
#             --SAVE_METRIC /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/evaluation_result/story_evaluation_single_data.json \
#             --DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/test.json \

# CUDA_VISIBLE_DEVICES=1 python model_evaluation.py \
#             --CUTOFF_LEN 1024 \
#             --MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
#             --LORA_CHECKPOINT_METRIC_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_mix_half_chatglm \
#             --SAVE_METRIC /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/evaluation_result/story_evaluation_max_half_data.json \
#             --DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/test.json \

CUDA_VISIBLE_DEVICES=1 python model_evaluation.py \
            --CUTOFF_LEN 1024 \
            --MODEL_NAME /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_mix_all_chatglm \
            --SAVE_METRIC /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/evaluation_result/story_evaluation_max_all_data.json \
            --DATA_PATH_TEST /mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/story_generation/test.json \

# python model_evaluation.py \
#             --CUTOFF_LEN 256 \
#             --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
#             --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
#             --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mix_data_generation_evaluation.json \
#             --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_generation.json \

# python model_evaluation.py \
#             --CUTOFF_LEN 256 \
#             --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
#             --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
#             --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mix_data_all_evaluation.json \
#             --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test.json \

# python model_evaluation.py \
#             --CUTOFF_LEN 256 \
#             --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
#             --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/mix_data_summarize_keywords_chatglm \
#             --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mix_summarize_keywords_data_generation_evaluation.json \
#             --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_generation.json \

# python model_evaluation.py \
#             --CUTOFF_LEN 256 \
#             --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
#             --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/mix_data_summarize_keywords_chatglm \
#             --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mix_summarize_keywords_data_appreciation_evaluation.json \
#             --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_appreciation.json \