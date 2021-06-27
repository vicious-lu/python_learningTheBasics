#defining a tuple, it uses '()' instead of '[]' from a list
fruits = ("oranges", "bananas", "grapes")
print(fruits)

#lenght of a tuple
print(len(fruits))
print("\n\n")

#with an index
print(fruits[0])
print("\n\n")

#all that we see in lists applies to tuples except adding elemtns and deleting them

#print all elements separated with no format of list
for tuple in fruits:
    print(tuple, end = ' ') # we can add whatever we want in "end = ''" to end with between prints
print("\n\n")

#convert a tuple to a list
print(fruits)
listFruits = list(fruits)
listFruits[0] = 'apples'
#fruits = tuple(listFruits)
#print(fruits)