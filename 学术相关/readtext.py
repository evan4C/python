import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_table('122004-pre.txt', sep=', ', header=None, skiprows=17)
a = data.set_index(0)

a.plot()
plt.show()

