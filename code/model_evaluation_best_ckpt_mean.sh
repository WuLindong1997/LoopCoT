python model_evaluation_best_ckpt_mean.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/mix_data_summarize_keywords_chatglm \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/more_data_appreciation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_appreciation.json \
            --CKPT  checkpoint-29000\
            
python model_evaluation_best_ckpt_mean.py \
            --CUTOFF_LEN 256 \
            --MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
            --LORA_CHECKPOINT_METRIC_DIR /root/autodl-tmp/wld/model/lora_check_point/mix_data_summarize_keywords_chatglm \
            --SAVE_METRIC /root/autodl-tmp/wld/evaluation_result/more_data_generation.json \
            --DATA_PATH_TEST /root/autodl-tmp/wld/data/tmp/test_generation.json \
            --CKPT  checkpoint-29000\


