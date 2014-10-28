#create best_wishes

#list of songs
import wikipedia
abc = ['KISS ON MY LIST, HALL & OATES', "JESSIE'S GIRL, RICK SPRINGFIELD" , 'JACK AND DIANE, JOHN COUGAR MELLENCAMP'] 
i = 0

aka = wikipedia.page(abc[i])
best_wishes = open("best_wishes", "w")
best_wishes.write(aka.content.encode('utf-8'))

while i < len(abc):

	aka = wikipedia.page(abc[i])
	best_wishes = open("best_wishes", "a+")
	best_wishes.write(aka.content.encode('utf-8'))
	best_wishes.close()
	
	i = i+1
# from topia.termextract import extract
# extractor = extract.TermExtractor()

#high repeated


