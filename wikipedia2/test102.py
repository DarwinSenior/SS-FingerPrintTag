import wikipedia
abc = ["JESSIE'S GIRL, RICK SPRINGFIELD"]
i = 0 
abc[i]



aka = wikipedia.page(abc)
best_wishes = open("best_wishes", "w")
best_wishes.write(aka.content.encode('utf-8'))

while i < len(abc):


	aka = wikipedia.page(abc[i])
	best_wishes = open("best_wishes", "a+")
	best_wishes.write(aka.content.encode('utf-8'))
	best_wishes.close()
	i=i+1


