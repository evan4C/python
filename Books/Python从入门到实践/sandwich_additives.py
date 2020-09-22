sandwiches_additives = ['spicy', 'salt', 'suger', 'vinegar']

def sandwiches_additive(*intergradients):
	print('Here are the sandwiches_additives in ur sandwich:')
	for additive in intergradients:
		print (additive)
	print('------')

sandwiches_additive(sandwiches_additives)