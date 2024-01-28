import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 给定数据
data = [0.418035926, 0.441520012, 0.458145562, 0.925671919, 1.25015437, 1.526433752, 1.547718321, 1.569011275,
        1.620057989, 1.824822256, 1.904477896, 2.043180113, 2.098093026, 2.183826528, 2.240002036, 2.326788073,
        2.749436941, 2.783348284, 2.83947022, 3.223881218]

# 计算均值和标准差
mean = np.mean(data)
std = np.std(data)

# 生成正态分布曲线的x轴数据
x = np.linspace(min(data), max(data), 100)

# 计算正态分布曲线的y轴数据
y = norm.pdf(x, mean, std)

# 绘制直方图和正态分布曲线
plt.hist(data, bins=8, density=True, alpha=0.5, label='Data')
plt.plot(x, y, 'r', label='Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()

# 计算3 sigma附近的值
lower_bound = mean - 3 * std
upper_bound = mean + 3 * std

# 计算0.95附近的值
percentile = norm.ppf(0.95, mean, std)

# 打印结果
print(f'3 sigma附近的值：{lower_bound} - {upper_bound}')
print(f'0.95附近的值：{percentile}')

# 显示图形
plt.show()
