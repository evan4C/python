import matplotlib.pyplot as plt

GDP = [122,133,98,97]

plt.bar(range(4),GDP,align = "center",color = "blue",alpha = 0.8)

plt.ylabel('GDP')

plt.title('GDP comparation')

plt.xticks(range(4),['beijing','shanghai','tianjin','chongqin'])

plt.ylim([50,150])

for x, y in enumerate(GDP):
    plt.text(x, y+5, '%s' % round(y, 1), ha='center')

plt.show()

