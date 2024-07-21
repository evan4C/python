import pandas as pd
import matplotlib.pyplot as plt

header = ['time', 'current']
data = pd.read_table('pre.txt', names=header, sep=',')

plt.plot(data['time'], data['current']*1000/0.196)

plt.title('current-time curve')
plt.xlabel("Time(s)")
plt.ylabel('Current(mA/cm2)')

plt.tick_params()
plt.show()





