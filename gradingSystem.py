#code for give a grade to a given score
score = int(input('provide a score: '))
grade = ''
if score == 9 or score == 10:
    grade = 'A'
elif score == 8:
    grade = 'B'
elif score == 7:
    grade = 'C'
elif score == 6:
    grade = 'D'
elif score <= 5:
    grade = 'F'
else:
    grade = 'grade value unknow'

print(grade)