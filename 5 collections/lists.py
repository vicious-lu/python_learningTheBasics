#define list with names
names = ['Luis', 'Karla', 'Richard', 'Maria'] #can contain different data types
#printing the list
print(names) #this prints the list
print("\n\n")

#access different index in order
print(names[0])   # -> Luis   
print(names[1])   # -> Karla
#inverse order
print(names[-2])  # -> Richard
print(names[-1])  # -> Maria
print("\n\n")

#print a range
print(f'setting two elements in ranges: \n{names[0:2]}\n')   #Luis(0), Karla(1); without Richard(3)
print(f'setting one element on the right: \n{names[:3]}\n')    #this way is from the beginning od the list to the 3
print(f'setting one element at the left: \n{names[1:]}')    #this way is form the index 1 to the end of the list
print("\n\n")

#lenght of a list
print(len(names))
print("\n\n")

#adding elements to a list
names.append('Charlie')
print(names)        #Now here is Charlie
#another way to, now telling an index
names.insert(1, 'Added with insert in 1')
print(names)        #karla was moved to the right
print("\n\n")

#removing elements from a list
names.remove('Added with insert in 1')
print(names)
#another way
names.pop()     #this removes the last element added to the list
print(names)
#del function
del names[0]    #this removes the selected index
print(names)
#removing all elements of the list
names.clear()
print(names)
#delete from memory
del names
#print(names)    #this will cause an error because we just deleted the list from memory