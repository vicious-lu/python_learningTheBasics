class Person:
    def __init__(self, name, surname, age) -> None:
        self.__name = name # if we want to really protect the data we need to use __ before an atribute
        self.surname = surname
        self.age = age

    def tellData(self):
        print(f'name: {self.__name} \nsurname: {self.surname} \nage: {self.age}')

    pass

person1 = Person('Joel', 'Lopez', 45)
person1.__name = 'Luis'

person1.tellData()
print('\n\n')


#Get and Set _______________________________________________________________________________________________________
class PersonWithGetAndSet:
    def __init__(self, name, surname, age) -> None:
        self._name = name # if we want to really protect the data we need to use __ before an atribute
        self._surname = surname
        self._age = age
    
    @property  #this is for setting the method name() like an atribute
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    @name.setter #this way we can still change the atribute
    def name(self, name):
        self._name = name

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @age.setter
    def age(self, age):
        self._age = age
    #if we dont add a set method for an atribute, its called a read only atribute

    def tellData(self):
        print(f'name: {self._name} \nsurname: {self._surname} \nage: {self._age}')

    pass

person2 = PersonWithGetAndSet('Luis', 'Saucedo', 23)
print(person2.name) #theres no atribute called name and we still can use it like so
#now that we have a setter we can change the atribute normally
person2.name = 'Alejandro'
person2.surname = 'Devora'
person2.age = '56'
print(person2.name, person2.surname, person2.age)