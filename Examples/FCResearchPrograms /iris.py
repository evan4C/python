import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')

spec = iris.species.unique()

for i in range(3):
    plt.plot(iris.loc[iris.species=spec[i], 'petal_length'],
    iris.loc[iris.species=spec[i], 'petal_width'],
    label=spec[i])

plt.tick_params(top='off', right='off')
plt.legend(loc='upper left')
plt.show()
