class IODevice:
    def __init__(self, entryType, brand) -> None:
        self._entryType = entryType
        self._brand = brand

    def __str__(self) -> str:
        return f'IODevice: [ Entry Type: {self.entryType}, Brand: {self.brand} ]'

    @property
    def entryType(self):
        return self._entryType

    @entryType.setter
    def entryType(self, a):
        self._entryType = a

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, a):
        self._brand = a
    