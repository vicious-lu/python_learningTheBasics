class Product:
    product_counter = 0

    def __init__(self, name, price) -> None:
        Product.product_counter += 1
        self._productId = Product.product_counter
        self._name = name
        self._price = price

    def __str__(self) -> str:
        return f' Product: [ Product ID: {self._productId}, Name: {self._name}, Price: {self._price} ] '
    
    @property
    def price(self):
        return self._price

if __name__ == '__main__':
    _______________product1 = Product('shirt', '100')
    print(_______________product1)