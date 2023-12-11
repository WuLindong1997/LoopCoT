import matplotlib.pyplot as plt
import os
os.chdir(os.path.dirname(__file__))


# 数据
categories = ['rouge-1', 'rouge-2', 'rouge-l', 'bleu-4']
single_data = [30.52, 7.16, 18.36, 6.10]
mix_all_data = [31.25, 7.21, 18.99, 6.14]
mix_half_data = [32.12, 7.74, 19.18, 6.46]

# 绘制柱状图
bar_width = 0.19
index = range(len(categories))
plt.bar(index, single_data, width=bar_width, label='Single', color='skyblue', edgecolor='black', linewidth=1, alpha=0.7)
plt.bar([i + bar_width for i in index], mix_all_data, width=bar_width, label='Mix All', color='lightgreen', edgecolor='black', linewidth=1, alpha=0.7)
plt.bar([i + 2 * bar_width for i in index], mix_half_data, width=bar_width, label='Mix Half', color='lightcoral', edgecolor='black', linewidth=1, alpha=0.7)
# 设置图表属性
plt.xlabel('Metrics')
plt.ylabel('Scores')
plt.title('Comparison of Different Training Data Models')
plt.xticks([i + bar_width for i in index], categories)
plt.legend()
plt.tick_params(axis='y', direction='in', length=3, width=1)
plt.tick_params(axis='x', direction='in', length=3, width=1)


# 显示图表
plt.show()
plt.savefig('../../evaluation_result/story_result.png',dpi = 900)
