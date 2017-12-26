import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

titanic = pd.read_csv('titanic_train.csv')
titanic.dropna(subset=['Age'], inplace=True)

# 提取不同性别的年龄数据
age_female = titanic.Age[titanic.Sex == 'female']
age_male = titanic.Age[titanic.Sex == 'male']

plt.hist(age_female, bins=np.arange(titanic.Age.min(), titanic.Age.max(), 2), label='女性', color='blue', edgecolor='k')
plt.hist(age_male, bins=np.arange(titanic.Age.min(), titanic.Age.max(), 2), label='男性', color='steelblue',
         edgecolor='k', alpha=0.6)

plt.title('乘客年龄直方图')
plt.xlabel('年龄')
plt.ylabel('人数')

plt.tick_params(top='off', right='off')

plt.legend(loc='best')

plt.show()
