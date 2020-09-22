import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

titanic = pd.read_csv('titanic_train.csv')

titanic.dropna(subset=['Age'], inplace=True)

# 绘图：乘客年龄的累计频率直方图
plt.hist(titanic.Age,  # 绘图数据
        bins=np.arange(titanic.Age.min(), titanic.Age.max(), 5),  # 指定直方图的组距
        normed=True,  # 设置为频率直方图
        cumulative=True,  # 积累直方图
        color='steelblue',  # 指定填充色
        edgecolor='k',  # 指定直方图的边界色
        label='直方图')  # 为直方图呈现标签

# 设置坐标轴标签和标题
plt.title('乘客年龄的频率累计直方图')
plt.xlabel('年龄')
plt.ylabel('累计频率')

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off', right='off')

# 显示图例
plt.legend(loc='best')
# 显示图形
plt.show()
