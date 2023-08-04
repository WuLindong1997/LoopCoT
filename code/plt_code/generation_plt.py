import matplotlib.pyplot as plt
import json

# 从文件中读取数据
with open('/root/autodl-tmp/wld/evaluation_result/mix_data_appreciation_evaluation.json', 'r') as f:
    data1 = json.load(f)
with open('/root/autodl-tmp/wld/evaluation_result/single_data_appreciation_evaluation.json', 'r') as f:
    data2 = json.load(f)

# 提取 ROUGE 和 BLEU 数据
rouge1_scores1 = [d['rouge-1'] for d in data1][:14]
rouge2_scores1 = [d['rouge-2'] for d in data1][:14]
rougeL_scores1 = [d['rouge-l'] for d in data1][:14]
bleu4_scores1 = [d['bleu-4'] for d in data1][:14]

rouge1_scores2 = [d['rouge-1'] for d in data2]
rouge2_scores2 = [d['rouge-2'] for d in data2]
rougeL_scores2 = [d['rouge-l'] for d in data2]
bleu4_scores2 = [d['bleu-4'] for d in data2]

# 创建一个 2x2 的子图
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 绘制 ROUGE-1 折线图
axs[0, 0].plot(rouge1_scores1, label='Mix Data')
axs[0, 0].plot(rouge1_scores2, label='Single Data')
axs[0, 0].set_xlabel('Checkpoint')
axs[0, 0].set_ylabel('ROUGE-1 Score')
axs[0, 0].set_title('Comparison of ROUGE-1 Scores')
axs[0, 0].legend()

# 绘制 ROUGE-2 折线图
axs[0, 1].plot(rouge2_scores1, label='Mix Data')
axs[0, 1].plot(rouge2_scores2, label='Single Data')
axs[0, 1].set_xlabel('Checkpoint')
axs[0, 1].set_ylabel('ROUGE-2 Score')
axs[0, 1].set_title('Comparison of ROUGE-2 Scores')
axs[0, 1].legend()

# 绘制 ROUGE-L 折线图
axs[1, 0].plot(rougeL_scores1, label='Mix Data')
axs[1, 0].plot(rougeL_scores2, label='Single Data')
axs[1, 0].set_xlabel('Checkpoint')
axs[1, 0].set_ylabel('ROUGE-L Score')
axs[1, 0].set_title('Comparison of ROUGE-L Scores')
axs[1, 0].legend()

# 绘制 BLEU-4 折线图
axs[1, 1].plot(bleu4_scores1, label='Mix Data')
axs[1, 1].plot(bleu4_scores2, label='Single Data')
axs[1, 1].set_xlabel('Checkpoint')
axs[1, 1].set_ylabel('BLEU-4 Score')
axs[1, 1].set_title('Comparison of BLEU-4 Scores')
axs[1, 1].legend()

# 调整子图之间的间距
plt.subplots_adjust(wspace=0.3, hspace=0.3)

# 显示图形
plt.show()
fig.savefig('/root/autodl-tmp/wld/evaluation_result/appreciation_result.png')