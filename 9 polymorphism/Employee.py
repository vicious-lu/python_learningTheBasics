class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f'Employee: [ Name: {self.name}, Salary: {self.salary} ]'

    def printDetail(self):
        return self.__str__()