script_dir=$(dirname $(realpath $0))
project_dir=${script_dir}/..
cd ${project_dir}
N_GPU=2
EXPERIMENT="test_deepspeed_chatglm"
OUTPUT_DIR="model/lora_check_point/${EXPERIMENT}"
logging_dir=runs/${EXPERIMENT}
cmd="torchrun --nproc_per_node=${N_GPU} code/chatglm_train_lora.py \
    --MICRO_BATCH_SIZE 4 \
	--BATCH_SIZE 16 \
	--EPOCHS 30 \
	--LEARNING_RATE 2e-5 \
	--CUTOFF_LEN 256 \
	--LORA_R 16 \
	--MODEL_NAME model/chatglm2-6b \
	--OUTPUT_DIR ${OUTPUT_DIR} \
	--DATA_PATH_TRAIN data/generation/train.json \
	--DATA_PATH_TEST data/generation/test.json \
	--DATA_PATH_CACHE cache \
	--DATA_TYPE json \
	--SAVE_STEPS 100 \
    --EVAL_STEPS 100 \
    --DEEPSPEED code/deepspeed_config.json \
    "
mkdir -p ${logging_dir}
echo $cmd
$cmd | tee ${logging_dir}/log.txt