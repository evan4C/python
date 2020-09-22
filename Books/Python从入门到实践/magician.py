magicians = ['li', 'liu', 'wang', 'jen',]

def show_magicians(magicians):
	for magician in magicians:
		print ('the magician is: ' + magician)

show_magicians(magicians)

def make_great(magicians):

	for i in range(len(magicians)):
		magicians[i] += ' the Great'

	return magicians

great_magicians = make_great(magicians[:])

show_magicians(magicians)
show_magicians(great_magicians)
