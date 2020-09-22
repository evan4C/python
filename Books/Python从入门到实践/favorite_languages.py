favorite_languages = {
	'jen': 'python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'python',
}

name_list = ['jen', 'li', 'susan', 'phil']

for person in name_list:
	if person in favorite_languages.keys():
		print (person + '! thanks for your coorperation.\n')
	elif person not in favorite_languages.keys():
		print (person + '! please take the survey.\n')