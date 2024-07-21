import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100)
y1 = np.random.random_integers(1, 100, size=50)  # 生成一个形状为50的一维整数数组组
y2 = np.random.random_integers(1, 100, size=50)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置图框的大小
fig = plt.figure(figsize=(10, 6))

plt.plot(x, y1, linestyle='-', linewidth=2, color='steelblue', marker='o',
         markersize=3, markeredgecolor='k', markerfacecolor='blue', label='1st')

plt.plot(x, y2, linestyle='-', linewidth=2, color='red', marker='o',
         markersize=3, markeredgecolor='k', markerfacecolor='black', label='2nd')

plt.title('随机数折线图')
plt.tick_params(top='off', right='off')

plt.legend()
plt.show()
