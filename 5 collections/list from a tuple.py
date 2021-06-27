#define tuple
staticList = (13, 1, 8, 3, 2, 5, 8)
#creating a list
dinamicList = []

for number in staticList:
    if number < 5:
        dinamicList.append(number)

#printing the list
print(dinamicList)