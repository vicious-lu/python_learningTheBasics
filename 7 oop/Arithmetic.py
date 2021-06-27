class arithmetic:
    """
    This class is for add methods like addition, substraction,
    multiplication, etc.
    """
    def __init__(self, opA, opB) -> None:
        self.opA = opA
        self.opB = opB

    def add(self):
        return self.opA + self.opB

    def sub(self):
        return self.opA - self.opB

    def mul(self):
        return self.opA * self.opB

    def div(self):
        return self.opA / self.opB

#create objetct calculator
calculator = arithmetic(2,3)

#calling methods from calculator
print(f'addition: {calculator.add()}')
print(f'substraction: {calculator.sub()}')
print(f'multiplication: {calculator.mul()}')
print(f'divition: {calculator.div()}')

