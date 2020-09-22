sandwich_orders = ['pie', 'light', 'spicy', 'hot', 'pastrami', 'pastrami', 'pastrami',]

print ('Pastrami is sold out!')

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')


finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your ' + sandwich + ' sandwich.')

	finished_sandwiches.append(sandwich)

print('\n---finished sandwiches---')
for finished_sandwich in finished_sandwiches:
	print (finished_sandwich.title())