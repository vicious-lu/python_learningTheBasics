#code to check if a number is between some given range
min = 0
max = 10
value = int(input("enter a number: "))
if (value >= min) and (value <= max):           # min <= value <= max
    print(f'the value {value} is in range')
else:
    print(f'the value {value} is out of range')