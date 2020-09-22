favorite_places = {
	'jen': ['beijin', 'dalian', 'wuhan'],
	'li': ['nagoya', 'anyang'],
	'wu': ['chengdu', 'tokyo', 'new york'],
}

for person, places in favorite_places.items():
	print('\n' + person.title() + ' likes the cities of:')

	for place in places:
		print (place.title())