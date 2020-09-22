import json

filename = 'username.json'

try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input('what is ur name?')
	with open(filename) as f_obj:
		json.dump(username, f_obj)
		print ('we will remember u when u come back ' + username + '!')
else:
	print ('welcome back ' + username + '!')