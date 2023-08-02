python process_data.py \
	--poem_path /root/autodl-tmp/wld/data/poem_test_info.json \
    --type generation \
    --save_path /root/autodl-tmp/wld/data/generation/test.json

wait
python process_data.py \
	--poem_path /root/autodl-tmp/wld/data/poem_train_info.json \
    --type generation \
    --save_path /root/autodl-tmp/wld/data/generation/train.json

wait
python process_data.py \
	--poem_path /root/autodl-tmp/wld/data/poem_train_info.json \
    --type appreciation \
    --save_path /root/autodl-tmp/wld/data/appreciation/train.json

wait
python process_data.py \
	--poem_path /root/autodl-tmp/wld/data/poem_test_info.json \
    --type appreciation \
    --save_path /root/autodl-tmp/wld/data/appreciation/test.json

wait
python process_data.py \
	--poem_path /root/autodl-tmp/wld/data/poem_test_info.json \
    --type mix \
    --save_path /root/autodl-tmp/wld/data/mix/test.json

wait
python process_data.py \
	--poem_path /root/autodl-tmp/wld/data/poem_train_info.json \
    --type mix \
    --save_path /root/autodl-tmp/wld/data/mix/train.json

wait

