#define dictionary
dictionary = {
    'IDE' : 'Integrated Development Enviroment',
    'OOP' : 'Object Oriented Programming',
    'DBMS' : 'Database Management System'
}

#print a dictionary
print(dictionary)
print("\n")

#accessing elements of a dictionary
print(dictionary['IDE'])
#another way
print(dictionary.get('OOP'))
print("\n")

#modify elements
dictionary['IDE'] = 'Diferent meaning'
print(dictionary['IDE'])
print('\n')

#in a for
for term, value in dictionary.items(): #note that we used the method .items()
    print(term, value)
print('\n')
#just the keys
for term in dictionary.keys():
    print(term)
print('\n')
#just the meanings
for value in dictionary.values():
    print(value)
print('\n')

#check for existing element
print('IDE' in dictionary) #this is a boolean
print('\n')

#add elements to dictionary
dictionary['PK'] = 'Primary key'
print(dictionary)
print('\n')

#delete elements
dictionary.pop('PK')
print(dictionary)

#delete whole dictionary
del dictionary
print(dictionary) #this will cause an error