class Cube:
    def __init__(self, sLen1, sLen2, sLen3) -> None:
        self.sLen1 = sLen1
        self.sLen2 = sLen2
        self.sLen3 = sLen3

    def volume(self):
        return (self.sLen1 * self.sLen2 * self.sLen3)
    pass

#capture data from user to send to create the object
side1 = int(input("Give lenght of side1 (a): "))
side2 = int(input('Give lenght of side2 (b): '))
side3 = int(input('Give lenght of side3 (c): '))

#create object
minecraft = Cube(side1, side2, side3)
print('The volume of this figure is: ',minecraft.volume())
