from IOdevice import IODevice

class Keyboard(IODevice):

    keyboardCounter = 0

    def __init__(self, entryType, brand) -> None:
        super().__init__(entryType, brand)
        Keyboard.keyboardCounter += 1
        self._idKeyboard = Keyboard.keyboardCounter

    def __str__(self) -> str:
        return f'Keyboard: [ ID Mouse: {self._idKeyboard} ] {super().__str__()}'