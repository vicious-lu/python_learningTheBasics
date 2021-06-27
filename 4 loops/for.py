#basic structure
string = 'Hello'
for letter in string: #letter is a variable containing each letter form the string, string is an array of letters
    print(letter)
else:
    print('end of for cycle\n\n')

#a combination of for and if - else
for letter in 'Alejandro':
    if letter == 'a' or letter == 'A':
        print(f'letter found: {letter}')
        break #this breaks the for, including the else block
else:
    print('end of for cycle')