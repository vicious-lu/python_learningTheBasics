#basic if-else
condition = False
if condition:     #if condition is anything but False or an empty chain will triger the true block
    print("condition is true")
elif condition == False:
    print("condition is False")
else:
    print("condition not recognized")
print("\n\n")

#int to string
print('code to turn an int into a string: ')
#commented for smooth running:
#num = int(input("provide a number between 1 and 3: "))
num = 2 #added for smooth running
numString = ''
if num == 1:
    numString = "number one"
elif num == 2:
    numString = "number two"
elif num == 3:
    numString = "number three"
else:
    numString = "value out of range"
print(f'provided number: {num} : {numString}\n\n')

#simplified if-else, this only works for simple if else with small code
condition = True
print("condition is true") if condition else print('condition is false')