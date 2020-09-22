class Restaurant():

	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.n_reserved = 0

	def describe_restaurant(self):
		print("This is a " + self.type + '-type restaurant named by '
		 + self.name +'.')

	def open_restaurant(self):
		print('This restaurant is now running!')

	def number_of_customer(self):
		print ('there are ' + str(self.n_reserved) + ' people that have come to this restaurant.')

	def set_number_served(self, n_reserved):
		self.n_reserved = n_reserved
		print ('the number_of_customer has been updated to ' + str(self.n_reserved))

	def increment_number_served(self, n_reserved_incre):
		self.n_reserved += n_reserved_incre



restaurant1 = Restaurant('tai', 'tailand')

restaurant1.number_of_customer()

restaurant1.n_reserved = 23

restaurant1.number_of_customer()

restaurant1.set_number_served(56)

restaurant1.increment_number_served(10)

restaurant1.number_of_customer()