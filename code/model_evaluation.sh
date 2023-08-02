python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/single_data_appreciation_evaluation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_appreciation.json \
            
python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/single_data_generation_evaluation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_generation.json \

python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mix_data_appreciation_evaluation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_appreciation.json \

python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mix_data_generation_evaluation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_generation.json \

python model_evaluation.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/mix_data_all_evaluation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test.json \