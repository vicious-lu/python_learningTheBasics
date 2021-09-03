class Monitor:

    monitorCounter = 0

    def __init__(self, brand, size) -> None:
        self.__brand = brand
        self.__size = size
        Monitor.monitorCounter += 1
        self.__idMonitor = Monitor.monitorCounter
        

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, a):
        self.__brand = a
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, a):
        self.__size = a
    
    def __str__(self) -> str:
        return f'Monitor: [ ID Monitor: {self.__idMonitor}, Brand: {self.__brand}, Size: {self.__size} ]  '