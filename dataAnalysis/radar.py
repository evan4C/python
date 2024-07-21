import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

values = [3.2, 2.1, 3.5, 2.8, 3]
values2 = [4,4.1,4.5,4,4.1]
feature = ['德', '智', '体', '美', '劳']

N = len(values)

angles = np.linspace(0, 2*np.pi, N, endpoint=False)

# 为了使雷达图一圈封闭起来，需要下面的步骤
values = np.concatenate((values, [values[0]]))
values2=np.concatenate((values2,[values2[0]]))
angles = np.concatenate((angles, [angles[0]]))

fig = plt.figure()
# 这里一定要设置为极坐标格式,111表示子图的位置
ax = fig.add_subplot(111, polar=True)
# 折线图
ax.plot(angles, values, 'o-', linewidth=2, label='1')
# 颜色
ax.fill(angles, values, alpha=0.25)

ax.plot(angles, values2, 'o-', linewidth=2, label='2')
ax.fill(angles, values2, alpha=0.25)

# 添加每个特征的标签
ax.set_thetagrids(angles * 180/np.pi, feature)
# 设置雷达图的范围
ax.set_ylim(0, 5)

plt.title('员工表现')
# 添加网格线
ax.grid(True)

plt.legend()
plt.show()
