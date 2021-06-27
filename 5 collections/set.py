#we define a set with '{}', this doesnt have an index, so it prints in random order everytime
planets = {'mercury', 'venus', 'earth', 'mars'}

#printing the set, random everytime by nature
print(planets)
print("\n\n")

#adding elements to sets
planets.add('neptune')
planets.add('pluto')

#if we add the same element twice we only have one in the set
planets.add('neptune')
planets.add('neptune')
planets.add('neptune')
print(planets)      #in a list planets will have neptune four times
print("\n\n")

#delete elements
planets.remove('pluto')
print(planets)
print("\n\n")

#delete whole set
del planets
print(planets)      #this will cause an error