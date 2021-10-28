'''
ID: mateibu1
LANG: PYTHON3
TASK: friday
'''


'''
1. Read the prompt
2. Read the prompt again
3. You will need to know if a given year is a leap year in order to
complete this problem, so write a function to determine so. It should look like "def is_leap_year(year)". Do not
Google for solutions on how to determine if a given year is a leap year. Follow the rules regarding leap years in the
bullet points and come up with the method yourself. If you get stuck, let us know.
4. Test your is_leap_year function against a handful of years (such as the ones listed in the prompt) to verify it works correctly
5. You will need to know how many days are in each month (on a non leap year). Store those values in a list
6. Make a function that takes a month and a year as arguments and returns the number of days in that month. It should look like
"def num_days(year, month)".
7. Loop over each month for a specified non-leap year (example: 1995), printing out the number of days in each month.
Loop over each month for a specified leap year (example: 2012), printing out the number
of days in each month. Make sure both are correct
'''




#f = open('friday.in', 'r')
#w = open('friday.out', 'w')

year = 1900
month_of_year = 0 #Janurary
date_of_month = 0 #First day of the month
day_of_week = 0 #Monday

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num_thirteens = [0,0,0,0,0,0,0] #must have 7 slots for how many days in a week
days = [0,1,2,3,4,5,6]
#Has to be divisible by 4
#If it is a century (divisible by 100) has to be divisible by 400
def is_leap_year(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return True
  return False

def days_in_month (month, year):
  if month == 1 and is_leap_year(year):
    return 29
  else:
    return months[month]


def next_day():
  global date_of_month, day_of_week, year, month_of_year
  date_of_month += 1
  day_of_week += 1
  if day_of_week == 7:
    day_of_week = 0
  if date_of_month > days_in_month(month_of_year,year):
    month_of_year += 1
    date_of_month = 0

for i in range(0,40):
  print(day_of_week, date_of_month)
  next_day()

def test():
  print(days_in_month(1, 2021) == 28)
  print(days_in_month(1, 2020) == 29)
  print(days_in_month(7, 2020) == 31)
#The days of the week recieve number values
#We use %7 to get the value of the day so we loop back
#test()
