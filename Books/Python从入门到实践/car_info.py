def car_info(maker, car_type, **customerize):
	profile = {}

	profile['maker'] = maker
	profile['type'] = car_type

	while customerize:
		for k, v in customerize.items():
			profile[k] = v
		break

	return profile

car01 = car_info('subaru','back')

car02 = car_info('toyota', 'canya', color='yellow', size='28')

print (car01,car02)

