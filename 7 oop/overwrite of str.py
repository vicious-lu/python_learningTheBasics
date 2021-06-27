from inheritance import *

person1 = Person('Raul', 'Vazquez', 45)
print(person1) #we allowed this with __str__

worker2 = Worker('Luis', 'Saucedo', 23, '23444')
print(worker2) #__str__ is modified