from operator import itemgetter

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
newList = itemgetter(0,2,4, 6, -2)(letters)


#print (list(newList))
print(letters[::2])
