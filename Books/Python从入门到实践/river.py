river = {'yellow river': 'China', 'amazon': 'Brizal', 'saina': 'france', 'yangzi': 'China'}

for k, v in river.items():
	print ('The ' + k + ' runs through ' + v.title() + '.')

print ('\n')

for name in sorted(river.keys()):
	print ('The river is ' + name + '.')

print ('\n')

for country in sorted(set(river.values())):
	print ('The countries are ' + country.title() + '.')