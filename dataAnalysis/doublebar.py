import matplotlib.pyplot as plt

import numpy as np

Y2016 = [15600,12700,11300,4270,3620]
Y2017 = [17400,14800,12000,5200,4020]

labels = ['SH', 'BJ', 'HK', 'SZ', 'GZ']

bar_width = 0.45

plt.bar(np.arange(5), Y2016, label='2016', color='steelblue', width=bar_width)
plt.bar(np.arange(5)+bar_width, Y2017, label='2017', color='indianred',width=bar_width)

plt.xlabel('city')
plt.ylabel('number of wealthy families')

plt.title('wealthy family in different cities')

plt.xticks(np.arange(5)+bar_width/2, labels)

plt.ylim([2500, 20000])

for x2016, y2016 in enumerate(Y2016):
    plt.text(x2016-bar_width/2, y2016+200, '%s' % y2016, va='center')

for x2017, y2017 in enumerate(Y2017):
    plt.text(x2017+bar_width/2, y2017+200, '%s' % y2017, va='center')

plt.legend()
plt.show()
