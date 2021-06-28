from Product import Product
from Order import Order

product1 = Product('shirt', 100)
product2 = Product('jeans', 300)
listOfProducts1 = [product1, product2]
order1 = Order(listOfProducts1)
order2 = Order(listOfProducts1)
print(order1)