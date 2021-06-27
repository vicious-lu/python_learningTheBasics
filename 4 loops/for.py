#basic structure
string = 'Hello'
for letter in string: #letter is a variable containing each letter form the string, string is an array of letters
    print(letter)
# else:
#     print('end of for cycle')

print("\n\n")

#a combination of for and if - else
for letter in 'Alejandro':
    if letter == 'a' or letter == 'A':
        print(f'letter found: {letter}')
        break #this breaks the for, including the else block
# else:
#     print('end of for cycle')

print("\n\n")

#continue and range function
print('even values:')
for i in range(6):
    if i % 2 == 0:
        print(i)
    continue # this ignores the rest of the for and goes to the next iteration
    print('I will never get to console.') #thats why this never gets to console
print('odd values:')
for i in range(6):
    if i % 2 != 0:
        print(i)
    continue # this ignores the rest of the for and goes to the next iteration
    print('I will never get to console.') #thats why this never gets to console