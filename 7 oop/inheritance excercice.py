class Vehicle:
    def __init__(self, wheels, color) -> None:
        self.wheels = wheels
        self.color = color

    def __str__(self) -> str:
        return f'Vehicle: [ Wheels: {self.wheels}, Color: {self.color} ]'

    def move(self):
        print(f'Moving Vehicle: [ Name: {self.name} ]')

class Car(Vehicle):
    def __init__(self, wheels, color, seats, name, velocity) -> None:
        super().__init__(wheels, color, seats, name)
        self.velocity = velocity

    def __str__(self) -> str:
        return f'Car: [ Velocity: {self.velocity} ] {super().__str__()}'

class Byke(Vehicle):
    def __init__(self, wheels, color, type) -> None:
        super().__init__(wheels, color)
        self.type = type

    def __str__(self) -> str:
        return f'Byke: [ Type: {self.type} ] {super().__str__()} '

if __name__ == '__main__':
    bicycle999999 = Byke(2, 'red', 'mountain')
    print(bicycle999999)