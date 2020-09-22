import json

filename = 'numbers.json'

with open(filename) as f_obj:
	unmbers = json.load(f_obj)

print (unmbers)