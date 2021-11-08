####### Data types/type conversion #######
s = 'Hello'
# 1. What is the data type of s?
i = 1
# 2. What is the data type of i?
f = 1.0
# 3. What is the data type of f?
b = True
# 4. What is the data type of b?

i_plus_f = i + f
# 5. What is the data type of i_plus_f?

# read a number from std input with the following line:
num = input('Type a number: ')
# 6. What is the data type of num?

# 7. What, if anything, must be done first in order to make the following line work?
num += i

####### Functions and return values #######
def foo(x):
    return (3 * x) + 2
def bar(x):
    print(str((3 * x) + 2))
# For the following questions, assume we call foo and bar with the argument x of type int
# 1. Between foo and bar, which function(s) has a return type? What type?
print(foo(2))
print(bar(2))
# 2. What will be the output from these print lines?
def isEven(x):
    if x % 2 == 0:
        return True
print(isEven(2))
print(isEven(1))
# 3. What is the output from these print lines?

####### If, else, elif #######
from random import randint
x = randint(0, 100)
print(x)
# 1. Using each of the keywords (if, else, and elif), turn the following into code:
# if x is even, print 'Even'
# otherwise if x is less than 50, print 'Small odd'
# otherwise, print 'Big odd'

####### Nested for loops #######
for i in range(5): # outer loop
    for j in range(3): # inner loop
        print(i + j)
# 1. How many times will the outer loop run?
# 2. How many lines will be printed?

# 3. Write a nested for loop that prints a 5x5 square of # signs like so:
#####
#####
#####
#####
#####

# 4. Write a nested for loop that prints a triangle of # signs like so:
#
##
###
####
#####

# Hint: for #3 and #4, use print('#', end='') so you don't automatically include a newline each time you call print
