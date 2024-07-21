import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel('货运.xls')

plt.bar(np.arange(8), data.loc[0, :][1:], color='red', label='realway', align='center')

plt.bar(np.arange(8), data.loc[1, :][1:], bottom=data.loc[0, :][1:], color='steelblue', label='road', align='center')

plt.bar(np.arange(8), data.loc[2, :][1:], bottom=data.loc[0, :][1:]+data.loc[1, :][1:], color='green', label='river', align='center')

plt.bar(np.arange(8), data.loc[3, :][1:], bottom=data.loc[0, :][1:]+data.loc[1, :][1:]+data.loc[2, :][1:], color='black', label='air', align='center')

plt.xlabel('month')
plt.ylabel('amount')
plt.title('amount per month')

plt.xticks(np.arange(8), data.columns[1:])

plt.ylim([0, 500000])

plt.legend(loc='upper center', ncol=4)

plt.show()
