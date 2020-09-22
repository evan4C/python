from random import randint

class Die():

	def __init__(self):
		self.sides = 6

	def roll_die(self,times):
		for i in range(times):
			print (randint(1,self.sides))

	def change_sides(self, sides):
		if sides <= 0:
			print ('please input a correct number!')
		else:
			self.sides = sides

die01 = Die()
die01.roll_die(10)

die02 = Die()
die02.change_sides(10)
die02.roll_die(20)

