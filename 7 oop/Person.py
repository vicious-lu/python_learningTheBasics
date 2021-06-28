from encapsulation import PersonWithGetAndSet
from constants import Math

#the file gets its name for the class were creating_________________________________________________________
class Person:
    def __init__(self,): #kind of a contructor
        self.name = 'Luis'
        self.surname = 'Saucedo'
        self.age = 23
    

person1 = Person() #this calls the constructor
print(person1.name) #this prints "Luis"
print(person1.surname) #this prints "Saucedo"
print(person1.age) #this prints 23
print('\n')


#in this case were telling that we need 3 arguments for creating an object__________________________________
class AnotherPerson:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        

person2 = AnotherPerson('Luis', 'Saucedo', 23) #here we define the data for the object
print(person2.name) #this prints "Luis"
print(person2.surname) #this prints "Saucedo"
print(person2.age) #this prints 23
print('\n')

person3 = AnotherPerson('Fredrich', 'Nietzsche', 34)
print(person3.name) 
print(person3.surname) 
print(person3.age) 
print('\n')

#change atributes of an object
person2.age = 60
print(person2.age)

#adding methods to classes


#this class has a method to print its data_____________________________________________
class PersonWithMethods:
    def __init__(self, name, surname, age, *args, **kargs):
        self.name = name
        self.surname = surname
        self.age = age
        self.args = args
        self.kargs = kargs


    def tellData(self):
        print(f'''
name    =   {self.name}
surname =   {self.surname}
age     =   {self.age}
args    =   {self.args}
kargs   =   {self.kargs}
        ''')



person4 = PersonWithMethods('Luis', 'Saucedo', 23)
person4.tellData()

person5 = PersonWithMethods('George', 'Washington', '45', 'element1', 45, 'element3', 56, 'element4', OK = '0 Kills', LOL = 'Laughting Out Loud')
person5.tellData()
print('\n')

#we can also use the method from the object and pass the object as a reference
# PersonWithMethods.tellData(person4)

#we can add atributes on the go
# person4.cellphone = 6567049006 #this is not on the class
# print(person4.cellphone)

person6 = PersonWithGetAndSet('Luis', 'Saucedo', 23)
del person6


#static methods and class methods
class ExampleStaticMethods:
    classVariable = 'Class Variable Value'

    def __init__(self, instanceVariable) -> None:
        self.instanceVariable = instanceVariable
    
    @staticmethod
    def staticMethod(): #this cant access self data
        print(ExampleStaticMethods.classVariable)

    @classmethod
    def classMethod(cls):
        print(cls.classVariable)

    def instanceMethod(self):
        self.classMethod()
        self.staticMethod()
        print(self.classVariable)
        print(self.instanceVariable)

if __name__ == '__main__':
    ExampleStaticMethods.staticMethod()
    ExampleStaticMethods.classMethod()

    myObject = ExampleStaticMethods('instance value')
    myObject.classMethod()
    myObject.staticMethod()


#constants in classes
print(Math.PI)