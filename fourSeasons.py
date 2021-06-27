#code to tell the season of a given month
month = int(input('provide a month of the year (1-12): '))
season = None
if  month == 1 or month == 2 or month == 12:
    season = 'winter'
elif month == 3 or month == 4 or month == 5:
    season = 'spring'
elif month == 6 or month == 7 or month == 8:
    season = 'summer'
elif month == 9 or month == 10 or month == 11:
    season = 'fall'
else:
    season = 'incorrect month format'

print(f'for month: {month} the season is: {season}')