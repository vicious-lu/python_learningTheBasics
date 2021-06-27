#define functions
def addAll(*args):
    count = 0      #counter
    for num in args:
        count += num
    return count

def mulAll(*args):
    count = 1
    for num in args:
        count *= num
    return count

#calling functions
print(addAll(2,3,4,5,6))
print(mulAll(1,2,3,4,5,6,7))