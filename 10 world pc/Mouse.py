from IOdevice import IODevice

class Mouse(IODevice):

    mouseCounter = 0

    def __init__(self, entryType, brand) -> None:
        super().__init__(entryType, brand)
        Mouse.mouseCounter += 1
        self._idMouse = Mouse.mouseCounter
    
    def __str__(self) -> str:
        return f'Mouse: [ ID Mouse: {self._idMouse} ] {super().__str__()}'