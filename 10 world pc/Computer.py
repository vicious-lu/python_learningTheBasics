
class Computer:

    computerCounter = 0

    def __init__(self, name, monitor, keyboard, mouse) -> None:
        Computer.computerCounter += 1
        self._IdComputer = Computer.computerCounter
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    def __str__(self) -> str:
        return f' Computer: [ ID: {self._IdComputer}, Name: {self._name}, Monitor: {self._monitor}, Keyboard: {self._keyboard}, Mouse: {self._mouse} ]'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a):
        self._name = a
    
    @property
    def monitor(self):
        return self._monitor
    
    @monitor.setter
    def monitor(self, a):
        self._monitor = a
    
    @property
    def keyboard(self):
        return self._keyboard
    
    @keyboard.setter
    def keyboard(self, a):
        self._keyboard = a
    
    @property
    def mouse(self):
        return self._mouse

    @mouse.setter
    def mouse(self, a):
        self._mouse = a