class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __add__(self, other):
        return self.name + other.name
    
    def __sub__(self, other):
        return self.age - other.age

if __name__== '__main__':
    person1 = Person('Luis', 23)
    person2 = Person('Rogelio', 17)

    print(person1 + person2)
    print(person1 - person2)

# obj2 + obj2
# obj2.__add__(obj2)