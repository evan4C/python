import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
x = np.linspace(0, 100)
y1 = np.random.random_integers(1, 100, size=50)  # 生成一个形状为50的一维整数数组组
y2 = np.random.random_integers(1, 100, size=50)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.scatter(x, y1, s=30, c='blue', marker='s', label='1')

plt.scatter(x, y2, s=30, c='red', marker='o', label='2')

plt.legend(loc='upper right')
plt.show()
