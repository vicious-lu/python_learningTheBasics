class Person:
    person_counter = 0

    @classmethod
    def generateNextValue(cls):
        cls.person_counter += 1
        return cls.person_counter

    def __init__(self, name, age) -> None:
        Person.person_counter += 1
        self.person_id = Person.generateNextValue()
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Person: [ ID: {self.person_id}, Name: {self.name}, Age: {self.age} ]'

    pass

if __name__ == '__main__':
    ________test = Person('Luis', 23)
    print(________test)