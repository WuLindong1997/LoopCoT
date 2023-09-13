import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Config of ChatGLM2-lora")

    parser.add_argument("--MICRO_BATCH_SIZE", type=int, default=4, help="Per device train batch size")
    parser.add_argument("--BATCH_SIZE", type=int, default=16, help="batch size")
    parser.add_argument('--EPOCHS', type=int, default=30, help='Training epochs')
    parser.add_argument('--WARMUP_STEPS', type=int, default=100, help='Warmup steps')
    parser.add_argument('--EVAL_STEPS', type=int, default=100, help='Eval_step')

    parser.add_argument('--LEARNING_RATE', type=float, default= 2e-5 , help='Training learning rate')
    parser.add_argument('--CUTOFF_LEN', type=int, default=256, help='Truncation length')
    parser.add_argument('--LORA_R', type=int, default=16, help='Lora low rank')
    parser.add_argument('--LORA_ALPHA', type=int, default=16, help='Lora Alpha')
    parser.add_argument('--LORA_DROPOUT', type=float, default=0.05, help='Lora dropout')

    parser.add_argument('--MODEL_NAME', type=str, default="/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/chatglm2-6b", help='Model name')
    parser.add_argument('--LOGGING_STEPS', type=int, default=100, help='Logging steps in training')
    parser.add_argument('--OUTPUT_DIR', type=str, default="/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_single_chatglm", help='Output dir')
    parser.add_argument('--DATA_PATH_TRAIN', type=str, default="/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/generation/train.json", help='Input dir')
    parser.add_argument('--DATA_PATH_TEST', type=str, default="/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/data/generation/test.json", help='Input dir')
    parser.add_argument('--DATA_PATH_CACHE', type=str, default="/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/cache", help='Input dir')
    parser.add_argument('--DATA_TYPE', type=str, choices= ["json" , "txt"], default="json", help='Input file type')
    parser.add_argument('--SAVE_STEPS', type=int, default=100, help='Save the model according to steps')
    parser.add_argument('--SAVE_TOTAL_LIMIT', type=int, default=1000, help='The number of the checkpoint you will save (Excluding the final one)')
    parser.add_argument('--SAVE_METRIC', type=str, default='/root/autodl-tmp/wld/evaluation_result/mix_data_evaluation.json', help='evalution')


    parser.add_argument('--TEMPERATURE', type=int, default=0, help='Temperature when inference')
    parser.add_argument('--LORA_CHECKPOINT_DIR', type=str, default="/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/model/lora_check_point/story_generation_single_chatglm/checkpoint-100", help='Your Lora checkpoint')
    parser.add_argument('--LORA_CHECKPOINT_METRIC_DIR', type=str, default="/root/autodl-tmp/wld/model/lora_check_point/mix_data_chatglm/", help='Your Lora checkpoint tital dir')
    parser.add_argument('--CKPT', type=str, default="che", help='checkpoint name')
    parser.add_argument('--DEEPSPEED_CONFIG_FILE', type=str, default="/mnt/vepfs/lingxin/Pretrain-data/wulindong/LoopCoT/config/deepspeed.json", help='deepspeed_config_file path')

    return parser.parse_args()