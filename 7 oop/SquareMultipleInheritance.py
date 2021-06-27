from Color import Color
from GeometricFigure import GeometricFigure

class Square(GeometricFigure, Color):
    def __init__(self, width, length, color) -> None:
        #super().__init__(width, length) this could cause issues due to multiple inheritance
        GeometricFigure.__init__(self, width, length)
        Color.__init__(self, color)

    def calculateArea(self):
        return self.width * self.length