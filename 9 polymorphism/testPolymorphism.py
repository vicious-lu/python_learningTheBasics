from Employee import Employee
from Manager import Manager

def printDetail(object):
    #print(object)
    print(type(object))
    print(object.printDetail())
    if isinstance(object, Manager):
        print(object.department)

employee1 = Employee('Luis', 13000)
printDetail(employee1)

manager1 = Manager('Luis', 15000, 'sales')
printDetail(manager1)