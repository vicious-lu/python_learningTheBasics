class GeometricFigure:
    def __init__(self, lenght, width) -> None:
        #simple validations, lenght
        if self._setterValidation(lenght):
            self._lenght = lenght
        else:
            self._lenght = 0
        
        #simple validations, width
        if self._setterValidation(width):
            self._width = width
        else:
            self.width = 0
    
    def __str__(self) -> str:
        return f'GeometricFigure: [ Lenght: {self._lenght}, Width: {self._width} ]'
    
    def _setterValidation(self, value):
        return True if 0 < value < 10 else False

    @property
    def lenght(self):
        return self._lenght
    
    @property
    def width(self):
        return self._width

    @lenght.setter
    def lenght(self, lenght):
        if self._setterValidation(lenght):
            self._lenght = lenght
        else:
            self._lenght = 0
    
    @width.setter
    def width(self, width):
        if self._setterValidation(width):
           self._width = width
        else:
            self._width = 0
    pass


class Color:
    def __init__(self, color) -> None:
        self._color = color
    
    def __str__(self) -> str:
        return f'Color: [ Color: {self._color} ]'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
    pass

class Square(GeometricFigure, Color):
    def __init__(self, lenght, width, color) -> None:
        GeometricFigure.__init__(self, lenght, width)
        Color.__init__(self, color)
    
    def __str__(self) -> str:
        # return f'Square: [ Lenght = {self._lenght}, Width = {self._width}, Color = {self._color}  ]'
        return f'{GeometricFigure.__str__(self)} {Color.__str__(self)}'

    def getArea(self):
        return self._width * self._lenght
    pass

class Rectangle(GeometricFigure, Color):
    def __init__(self, lenght, width, color) -> None:
        GeometricFigure.__init__(self, lenght, width)
        Color.__init__(self, color)
    
    def __str__(self) -> str:
        # return f'Rectangle: [ Lenght = {self._lenght}, Width = {self._width}, Color = {self._color}  ]'
        return f'{GeometricFigure.__str__(self)} {Color.__str__(self)}'

    def getArea(self):
        return self._width * self._lenght
    pass