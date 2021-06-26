#As simple as that:
print("Simple Print: ")
print("Hola mundo\n\n")
#With variables
word = "Hola mundo"
print(word)
word = 2      #The value can be changed during execution, and dont need to add a typo
print(word)
print("\n\n") #Only used to separate spaces

#Simple variable use
print("Using varibles to store the message:")
x = 10
y = 5
z = x + y
print(z)
print(x)
print(y)
print("\n\n")

#how to get the memory location of a variable
print("Getting memory location of each variable used in the section before and a new one:")
g = 2
print(id(g)) #this way it prints the memory location instead of the varibale stored itself
print(id(y))
print(id(x))
print(id(z))
print("\n\n")

#data types: int, string and bool
print("Data types and function (type):")
x = 10 #int
print("Int")
print("Value stored: ", x)
print("Result of type function: ", type(x), "\n") #to get and print data type of X
x = "Ten" #string
print("String")
print("Value stored: ", x)
print("Result of type function: ", type(x), "\n") #to get and print data type of X
x = True #bool, the first char must be Uppercase
print("bool")
print("Value stored: ", x)
print("Result of type function: ", type(x), "\n") #to get and print data type of X