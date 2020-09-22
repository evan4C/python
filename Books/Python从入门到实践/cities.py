cities = {
	'rome': {
	     'country': 'italy',
	     'population': '12000',
	     'fact': 'great city in the history.',
	},

	'anyang': {
	    'country': 'china',
	    'population': '50000',
	    'fact': 'hometown',
	},

	'nagoya': {
	    'country': 'japan',
	    'population': '3000',
	    'fact': 'work palce',
	},
}

for city in cities.keys():
	print ('\nThe name is: ' + city.title())

	print ('Country: ' + cities[city]['country'].title())
	print ('population: ' + cities[city]['population'])
	print ('fact: ' + cities[city]['fact'].title())