from Product import Product

class Order: 
    order_counter = 0

    def __init__(self, products) -> None:
        Order.order_counter += 1
        self._orderId = Order.order_counter
        self._products = list(products)

    def addProduct (self, product):
        self._products.append(product)
    
    def calculateTotal(self):
        total = 0
        for product in self._products:
            total += product.price
        return total
    
    def __str__(self) -> str:
        product_str = ''
        for product in self._products:
            product_str += product.__str__() + '|'

        return f'Order: {self._orderId}\nProducts: {product_str}'
    pass

if __name__ == '__main__':
    product1 = Product('shirt', 100)
    product2 = Product('jeans', 300)
    listOfProducts1 = [product1, product2]
    order1 = Order(listOfProducts1)
    print(order1)