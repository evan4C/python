import matplotlib.pyplot as plt

price = [12.2, 13.3, 11.4, 14.5, 15.6]

plt.barh(range(5), price, align='center', color='steelblue', alpha=0.1)

plt.xlabel('price')

plt.title("comparation")

plt.yticks(range(5), ['amazon', 'dangdang', 'jindong', 'taobao', 'tushu'])

plt.xlim([5, 20])

for x, y in enumerate(price):
    plt.text(y+1, x, '%s' % y, va='center')

plt.show()
