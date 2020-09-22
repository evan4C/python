import json

numbers = [1,2,3,4,5]

filenam = 'numbers.json'

with open (filename, 'w') as f_obj:
	json.dump(numbers, f_obj)