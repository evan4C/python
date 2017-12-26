import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

titanic = pd.read_csv('titanic_train.csv')
titanic.dropna(subset=['Age'], inplace=True)

plt.hist(titanic.Age, bins=np.arange(titanic.Age.min(), titanic.Age.max(), 5), color='blue', edgecolor='k', normed=True)

plt.title('乘客年龄频率直方图')
plt.xlabel('年龄')
plt.ylabel('频率')
plt.tick_params(top='off', right='off')

# 生成正态曲线的数据
x1 = np.linspace(titanic.Age.min(), titanic.Age.max(), 1000)
normal = mlab.normpdf(x1, titanic.Age.mean(), titanic.Age.std())
# 绘制正态分布曲线
line1, = plt.plot(x1, normal, 'r-', linewidth=2)

# 生成核密度曲线的数据
kde = mlab.GaussianKDE(titanic.Age)
x2 = np.linspace(titanic.Age.min(), titanic.Age.max(), 1000)
# 绘制
line2, = plt.plot(x2, kde(x2), 'g-', linewidth=2)

plt.legend([line1, line2], ['正态分布曲线', '核密度曲线'], loc='best')
plt.show()
