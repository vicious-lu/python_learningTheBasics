#typical factorial function for recursive functions
def factorial (arg):
    if arg == 1:
        return 1
    else:
        return arg * factorial(arg - 1)

print(factorial(5))

#print numbers from A to B descendent
def printN(arg):
    print(arg)
    if arg == 1:
        return
    printN(arg-1)

printN(5)
printN(3)