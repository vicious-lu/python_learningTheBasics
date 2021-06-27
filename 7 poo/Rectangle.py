class Rectangle:
    def __init__(self, lenght, breadth) -> None:
        self.length = lenght
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

#create test object
if __name__ == '__main__': #this way we prevent to have objects with the same name on this testing when using the modulus
    cellphone = Rectangle(56,23)
    print(f'the rectangle with lenght: {cellphone.length} and breadth: {cellphone.breadth} = {cellphone.area()}')