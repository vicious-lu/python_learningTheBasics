#simple input to a variable_____________________________________________
print("simple input to a variable: ") 
res = input("write some text: ") #returns a string
print("your input was: ",res,"\n\n")

#addition of two input numbers by user__________________________________
print("addition of two input numbers by user")
num1 = input("Enter the first number: ")
num2 = input("Enter the second numer: ")
result = num1 + num2
print("The addition result is: ", result,)
#the code used before returns a string, we need the int value
#for the next part to work we need to use integer numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second numer: "))
result = num1 + num2
print("The addition result is: ", result,"\n\n")