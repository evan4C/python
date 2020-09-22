def make_album(album_name, composer, songs=''):
	album = {
	    'album_name': album_name.title(),
	    'composer': composer.title(),
	}

	return album

while True:
 	print ('\nwhich album do you want us to know?')
 	print ('enter q to exit.')

 	album_name = input('album name is: ')
 	if album_name == 'q':
 		break
 	
 	composer = input('composer is: ')
 	if composer == 'q':
 		break

 	print ('\n---Album info---')
 	current = make_album(album_name, composer)
 	print (current)

