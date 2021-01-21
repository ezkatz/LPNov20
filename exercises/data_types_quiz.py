"""
This task is meant to review the basic data types. Feel free to run this code yourself
to make sure you understand/get the right answers

Basic Data Types:
string: a data type made up of characters. Anything surrounded by quotes is a string
  examples: 'hello world', 'five', '5'
  Notes:
    - using the + sign *concatenates* (fancy word for linking things together) two strings
    - no other sign (-, *, /, %, etc.) is applicable to strings
    - == for equality testing

int: data type of a whole number
  example: 0, 5, -23, 123456789012345678901234567890
  Notes:
    - Adding, subtracting, and multiplying work as expected. 2 types of division (/ and //)
    - Can do +=, -=, *=, /=, //=, etc.
    - Cannot do ++ or -- in python
    - Numbers ending in .0 (e.g. 5.0) are not ints, they are floats

float: data type of numbers that are rational but not ints
  examples: 2.5, -1.0, 0.0
  Notes:
     - This is the result of using the / operator (even if it's an even division like 8/4)
     - Having a .0 ending does not change it to an int
     - Using a float with an int for an addition, subtraction, multiplication, etc. makes the result a float

bool: A boolean value. Used in conditions for ifs, loops, and more
  examples: True, False, 1 == 0, 2 < 5
  Notes:
    - Only two values: True (note the capital T) and False
    - We can get these values through comparison operations (2 < 5)
    - We can flip the value with the ! operator
    - There are other operators we will learn about later

list: the python form of an array
  examples: l = [3, 5, 12], x = ['a', 'b', 'c'], z = [l, x, 'hello world']
  Notes:
    - 0-indexed, just like JavaScript
    - Lists have dynamic sizes (they can expand and shrink). Use len() to get length, append() to add (to the end)
    - List values do not need to be of the same type, and lists can contain other lists
    - Many other operations to do with lists

there are many others that we will learn about soon!
"""

a = input('Type in the number 5: ')
# Question 1: What is the data type of variable a at this point?

a = a + 3
a = a + '3'
# Question 2: Which one of the above statements is valid?
# Question 3: What is the value of variable a after executing the valid statement?

b = int(input('Type in the number 5: '))
# Question 4: What is the data type of variable b at this point?

b = b + 3
b = b + '3'
# Question 5: Which one of the above statements is valid?
# Question 6: What is the value of variable b after executing the valid statement?

# Question 7: What, if anything, do I need to do to turn variable a into a string?
# Question 8: What, if anything, do I need to do to turn variable b into a string?

c = 5
d = 4
e = c + d
# Question 9: What is the data type of e?

f = c / d
g = c // d
# Question 10: What is the data type and value of f?
# Question 11: What is the data type and value of g?

h = 5.0 + 4
# Question 12: What is the data type and value of h?

# Extra credit: What special function gives us the unicode value of a single character?
# example: the value of 'a' is is 97, the value of 'A' is 65, and the value of ' ' is 94?

'''
Ending Notes:
  We can always use the type() function to determine a variable's type
'''
