#the file gets its name for the class were creating_________________________________________________________
class person:
    def __init__(self,): #kind of a contructor
        self.name = 'Luis'
        self.surname = 'Saucedo'
        self.age = 23
    

person1 = person() #this calls the constructor
print(person1.name) #this prints "Luis"
print(person1.surname) #this prints "Saucedo"
print(person1.age) #this prints 23
print('\n')


#in this case were telling that we need 3 arguments for creating an object__________________________________
class anotherPerson:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        pass

person2 = anotherPerson('Luis', 'Saucedo', 23) #here we define the data for the object
print(person2.name) #this prints "Luis"
print(person2.surname) #this prints "Saucedo"
print(person2.age) #this prints 23
print('\n')

person3 = anotherPerson('Fredrich', 'Nietzsche', 34)
print(person3.name) 
print(person3.surname) 
print(person3.age) 
print('\n')

#change atributes of an object
person2.age = 60
print(person2.age)

#adding methods to classes


#this class has a method to print its data_____________________________________________
class personWithMethods:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        pass

    def tellData(self):
        print(f'''
name    =   {self.name}
surname =   {self.surname}
age     =   {self.age}
        ''')
        pass

person4 = personWithMethods('Luis', 'Saucedo', 23)
person4.tellData()

#we can also use the method from the object and pass the object as a reference
personWithMethods.tellData(person4)

#we can add atributes on the go
person4.cellphone = 6567049006 #this is not on the class
print(person4.cellphone)