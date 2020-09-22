nana = {
    'name': 'nana',
	'person': 'jen',
	'type': 'dog'
}

haha = {
    'name': 'haha',
	'person': 'li',
	'type': 'cat'
}

gogo = {
    'name': 'gogo',
	'person': 'new',
	'type': 'fish'
}

pets = [nana, haha, gogo]

for pet in pets:
	print ('\nName: ' + pet['name'])
	print ('Person: ' + pet['person'])
	print ('Type: ' + pet['type'])