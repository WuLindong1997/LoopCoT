python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mean_ckpt_single_appreciation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_appreciation.json \
            --CKPT  checkpoint-13500\
            
python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/generation_poem_chatglm2 \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mean_ckpt_single_generation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_generation.json \
            --CKPT  checkpoint-13500\

python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/mix_data_chatglm \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mean_ckpt_mix_appreciation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_appreciation.json \
            --CKPT  checkpoint-14000 \


python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/mix_data_chatglm \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mean_ckpt_mix_generation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_generation.json \
            --CKPT  checkpoint-14000 \

