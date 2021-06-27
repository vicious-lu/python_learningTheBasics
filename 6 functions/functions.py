# basic structure
def myFunction():
    print("hello from function")

# this is how you call myFunction()
myFunction()
# we always have to define the function before using it
print('\n')


# how to pass parameters to a function
def myFunctionWithParameters(name, surname):
    print(f'Name: {name}, Surname: {surname}')

myFunctionWithParameters('Luis', 'Saucedo')
myFunctionWithParameters('Rogelio', 'Saucedo') 
# with stepInto we can trace the value of the function in an IDE
print('\n')

# return in functions
def add(a, b):
    return a + b # we can tell what value to return

res = add(2,3)
print(res)
print(add(2,3)) #another way
print('\n')

#dafault values
#another way to define functions
# def add(a:int = 2, b:int = 2) -> int:
#     return a + b
def add(a = 0, b = 0): #are defined in the function
    return a + b

print(add())
print('\n')


#considerations in parameters
def listNames(*names): #* is for when we dont know how many elements we will send
    for name in names:
        print(name)

listNames('Luis Saucedo', 'Fred Jhones', 'Fredrich Nietzsche')
