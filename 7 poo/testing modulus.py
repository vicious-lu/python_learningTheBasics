#testing modulus, importing class rectangle
from Rectangle import Rectangle

amplifier = Rectangle(34, 20)
amplifier.area

#we can see form what modulus is running something
print(__name__) #using this line in the modulus
#if there was another object with the same name, at the time of printing
#it will print all that its set on the modulus file, with this line we can 
#identify from where is coming.