import pandas as pd
import matplotlib.pyplot as plt

header = ['potential', 'current']
data = pd.read_table('cv.txt', names=header, sep=',', skiprows=3684, nrows=2137)

plt.plot(data['potential']+0.311, data['current']*1000/0.196)

plt.title('Cyclic Voltammogram')
plt.xlabel("Potential(V vs. RHE)")
plt.ylabel('Current(mA/cm2)')

plt.tick_params()
plt.show()
