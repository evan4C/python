import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)

y = np.random.randint(10,30,10)

for i in range(20):

	plt.cla()
	plt.barh(x,y)
	plt.title(str(i))
	plt.yticks(x, list(map(lambda i: '%d mon'%i, x)))
	plt.pause(0.5)
	y = y+np.random.randint(0,5,10)

plt.show()