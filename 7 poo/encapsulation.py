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