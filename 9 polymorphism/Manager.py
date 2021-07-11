from Employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, department) -> None:
        super().__init__(name, salary)
        self.department = department

    def __str__(self) -> str:
        return f' {super().__str__()} Manager: [ Department: {self.department} ]'