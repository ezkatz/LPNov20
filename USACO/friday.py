"""
ID: 
LANG: PYTHON3
TASK: friday
"""

months = [
  31, # January
  28, # February
  31, # March
  30, # April
  31, # May
  30, # June
  31, # July
  31, # August
  30, # September
  31, # October
  30, # November
  31, # December
]

FEBRUARY = 1

# Leap Year: %4 except century, but %400 is
def is_leap_year(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
  if month == FEBRUARY and is_leap_year(year):
    return 29
  else:
    return months[month]

thirteenths = [0] * 7 # Equivalent to [0, 0, 0, 0, 0, 0, 0]

# Saturday = 0, Friday = 6
# 1/1/1900 = Monday
first_day = 2 # Which day of the week the first of the month is

# ----------------------------------------------
# - Everything above here is setting variables -
# - we need before we start the computation,   -
# - plus some helpful functions                -
# ----------------------------------------------

# Read from input
with open('friday.in', 'r') as fin:
  N = int(fin.readline().strip())

# Begin at 1st day of month
# Take note of which day of the week the 13th is
# Then move (# days in month) so we're now at the 1st of the next month
# Do so for each month of the specified number of years
for year in range(1900, 1900 + N):
  for month in range(len(months)):
    thirteenths[(first_day + 12) % 7] += 1
    first_day = (first_day + get_days_in_month(month, year)) % 7

# Write output in specified format
with open('friday.out', 'w') as fout:
  fout.write(str(thirteenths[0]))
  for i in range(1, 7):
    fout.write(' '  + str(thirteenths[i]))
  fout.write('\n')
