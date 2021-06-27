class Person:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self): #this method will work only when calling the object itself from a child
        return f'Person: [ name: {self.name}, surname: {self.surname} ]'

    def tellData(self):
        print(f'name: {self.name}\nsurname: {self.surname}\nage: {self.age}')
    
    pass

class Worker(Person):
    def __init__(self, name, surname, age, salary) -> None:
        super().__init__(name, surname, age) #this method initializes the data from the parent
        self.salary = salary
    
    def __str__(self):
        return f'Worker: [ Salary: {self.salary} ] {super().__str__()}' #addinig __str__ from parent and adding salary to it

if __name__ == '__main__':
    worker1 = Worker('John', 'Davis', 34, 32500)
    print(worker1.name)
