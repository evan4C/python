def Build_person(first_name, last_name, age=''):
	person = {
	     'first_name': first_name,
	     'last_name': last_name,
	}

	if age:
		person['age'] = age

	return person

li = Build_person('jen','li')

liu = Build_person('wang','liu', 27)

print (li)

print (liu)