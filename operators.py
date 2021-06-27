#A quick reminder of how to use operators
opA = 3
opB = 2
add = opA + opB
print(f'addition: {add} \n\n') #testing another syntax

#Substraction
sub = opA - opB
print(f'substraction: {sub}\n\n')

#Multiplication
mul = opA * opB
print(f'multiplication: {mul}\n\n')

#divition
div = opA / opB
print(f'divition: {div}\n\n')

#divition, int
div = opA // opB
print(f'divition (int): {div}\n\n')

#modulus
mod = opA % opB
print(f'modulus: {mod}\n\n')

#exponential
exp = opA ** opB
print(f'exponential: {exp}\n\n')

#assignation operator
print("assingation operator (and increment): ")
a = 1
print(a)
a = a + 1
print(a)
a+=1      #better way
print(a)
a-=2
print(a, "\n\n")

#comparation operators
a = 4
b = 4
print(f'a = {a}, b = {b}')
res = a == b #is a equal to b?
print(f'a == b  =   {res}')
res = a != b #is a different than b?
print(f'a != b  =   {res}')
res = a > b #is a major than b?
print(f'a > b   =   {res}')
res = a >= b #is a major or equal than b?
print(f'a >= b  =   {res}')
res = a < b #is a minor than b?
print(f'a < b   =   {res}')
res = a <= b #is a minor or equal than b?
print(f'a <= b  =   {res}\n\n')

#logic operators
a = True
b = False
print(f'a = {a}, b = {b}')
res = a and b
print(f'a and b =   {res}')
res = a or b
print(f'a or b =   {res}')
res = not a
print(f'not a   =   {res}')
res = not b
print(f'not b   =   {res}\n\n')

#check the age of someone to see the correct typo for them
age = int(input('enter your age: '))
twenties = age >= 20 and age < 30
thirties = age >= 30 and age < 40
print(f'Twenties: {twenties}')
print(f'thirties: {thirties}\n')
if twenties or thirties:
    print("You're on your 20's or 30's")
else:
    print("You're not on your 20's or 30's")