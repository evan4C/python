import matplotlib.pyplot as plt

# plt.style.use('ggplot')

edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
labels = ['中专', '大专', '本科', '硕士', '其他']

explode = [0, 0.1, 0, 0, 0]  # 用于突出显示大专学历人群

colors = ['#9999ff', '#ff9999', '#7777aa', '#2442aa', '#dd5555']

# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.axes(aspect='equal')  # 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆

plt.xlim([0, 4])
plt.ylim([0, 4])

# autopct 设置百分比的格式，这里保留一位小数
# wedgeprops 设置饼图内外边界的属性值
# textprops 设置文本标签的属性值
plt.pie(x=edu, explode=explode, labels=labels, colors=colors, autopct='%.1f%%', pctdistance=0.8,
        labeldistance=1.15, startangle=180, radius=1.5, counterclock=False,
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},
        textprops={'fontsize': 12, 'color': 'k'}, center=(1.8, 1.8), frame=1)

plt.xticks(())
plt.yticks(())

plt.title('credit on personal education level')

plt.show()