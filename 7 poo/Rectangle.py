class Rectangle:
    def __init__(self, lenght, breadth) -> None:
        self.length = lenght
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

#create test object
cellphone = Rectangle(56,23)

print(f'the rectangle with lenght: {cellphone.length} and breadth: {cellphone.breadth} = {cellphone.area()}')