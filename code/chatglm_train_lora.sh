#mix
python chatglm_train_lora.py \
	--MICRO_BATCH_SIZE 2\
	--BATCH_SIZE 14 \
	--EPOCHS 20 \
	--LEARNING_RATE 2e-5 \
	--CUTOFF_LEN 256 \
	--LORA_R 16 \
	--MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
	--OUTPUT_DIR /root/autodl-tmp/wld/model/lora_check_point/mix_data_chatglm \
	--DATA_PATH_TRAIN /root/autodl-tmp/wld/data/mix/train.json \
	--DATA_PATH_TEST /root/autodl-tmp/wld/data/mix/test.json \
	--DATA_TYPE json \
	--SAVE_STEPS 100 \
    --EVAL_STEPS 1000 \

wait
#appreciation
python chatglm_train_lora.py \
	--MICRO_BATCH_SIZE 2\
	--BATCH_SIZE 14 \
	--EPOCHS 20 \
	--LEARNING_RATE 2e-5 \
	--CUTOFF_LEN 256 \
	--LORA_R 16 \
	--MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
	--OUTPUT_DIR /root/autodl-tmp/wld/model/lora_check_point/apperation_poem_chatglm2 \
	--DATA_PATH_TRAIN /root/autodl-tmp/wld/data/appreciation/train.json \
	--DATA_PATH_TEST /root/autodl-tmp/wld/data/appreciation/train.json \
	--DATA_TYPE json \
	--SAVE_STEPS 100 \
    --EVAL_STEPS 1000 \

wait
#generation
python chatglm_train_lora.py \
	--MICRO_BATCH_SIZE 2\
	--BATCH_SIZE 14 \
	--EPOCHS 20 \
	--LEARNING_RATE 2e-5 \
	--CUTOFF_LEN 256 \
	--LORA_R 16 \
	--MODEL_NAME /root/autodl-tmp/wld/model/chatglm2-6b \
	--OUTPUT_DIR /root/autodl-tmp/wld/model/lora_check_point/generation_poem_chatglm2 \
	--DATA_PATH_TRAIN /root/autodl-tmp/wld/data/generation/test.json \
	--DATA_PATH_TEST /root/autodl-tmp/wld/data/generation/test.json \
	--DATA_TYPE json \
	--SAVE_STEPS 100 \
    --EVAL_STEPS 1000 \

