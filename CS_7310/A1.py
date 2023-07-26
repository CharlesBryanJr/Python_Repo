'''assignment 1'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
import math
import statistics as stats

print(" ")

'''
For each problem you need to write code for a function based on the requirements.
The function initally only contains the code 'pass' which does nothing
Your task is to write correct code that follows the coding guidelines.
In the cell following the code cell, the re are assertion statements that will test your code.
If there is an error, the assertion will throw an Error.
If you pass all the assertions, you will see the print statement display 'Passed'

Submit your notebook to Canvas in a zip file named as: a1.lastname.zip
'''

'''
Problem 1
Write two functions, 
is_odd() and is_even(), 
with a single numeric parameter n. 

The is_odd() function 
returns True if n is odd 
and False if n is even. 

The is_even() function 
returns the True if n is even 
and False if n is odd.

Both functions 
return False for numbers with fractional parts, 
such as 3.14 or -4.5.

Zero is considered an even number.

Floating-point numbers 
such as 3.1415 
are neither odd nor even, 
so both isOdd() and isEven() 
should return False for them.

Keep in mind that the isOdd() and isEven() function 
you write must return a Boolean
True or False value, 
not an integer 0 or 1. 
You need to use a == or != comparison operator 
to produce a Boolean value: 
7 % 2 == 1 evaluates to 1 == 1, 
which in turn evaluates to True.
'''

def is_odd(n):
    if isinstance(n, float) or n % 1 != 0:
        return False
    return True if n % 2 == 1 else False

def is_even(n):
    if isinstance(n, float) or n % 1 != 0:
        return False
    return True if n % 2 == 0 else False

print(is_odd(42) == False)
print(is_odd(9999) == True)
print(is_odd(-10) == False)
print(is_odd(-11) == True)
print(is_odd(3.1415) == True)
print(is_even(42) == True)
print(is_even(9999) == False)
print(is_even(-10) == True)
print(is_even(-11) == False)
print(is_even(3.1415) == False)
print("---")
print("---")
print("---")

'''
Problem 2
Write code for a function that 
returns True if n is a multiple of m, 
False otherwise
'''

def is_multiple_of(n, m):
    return True if n % m == 0 else False

print(is_multiple_of(100, 10) == True)
print(is_multiple_of(14, 3) == False)
print("---")
print("---")
print("---")

'''
Problem 3:
Write code for a function that 
returns the largest of three integers.
Do not use the logical and operator
Your code should handle
the case when 2 or 3 are the same max value
'''

def largest(a, b, c):
    return max(a, b, c)

print(largest(1, 2, 3) == 3)
print(largest(10, 99, 12) == 99)
print(largest(100, 99, 11) == 100)
print(largest(99, 99, 2) == 99)
print(largest(99, 2, 99) == 99)
print(largest(2, 2, 2) == 2)
print("---")
print("---")
print("---")

'''
Problem 4
Given two integer numbers 
return their product 
only if the product is equal to or lower than 1000, 
else return their sum.
'''

def sum_or_product(a,b):
    product = a*b
    if product <= 1000:
        return product
    return a + b

print(sum_or_product(5, 5) == 25)
print(sum_or_product(5, 1000) == 1005)
print("---")
print("---")
print("---")

'''
Problem 5
write a function convert(parm) such that:
if parm is an integer, 
    return the integer

if parm is a float, 
    return the floor value of the float

if parm is a string of all integers, 
    return the integer value
    note: for this assignment, 
    only strings of integers will be tested

if none of the above, 
    return None
'''

def convert(parm):
    if isinstance(parm, int):
        return parm
    elif isinstance(parm, float):
        return math.floor(parm)
    elif isinstance(parm, str):
        return int(parm)
    else:
        return None

print(convert(22) == 22)
print(convert(19.76) == 19)
print(convert("12345") == 12345)
print("---")
print("---")
print("---")

'''
Problem 6
Write a function loop(max, stop) that:
creates a for loop 
that iterates over numbers 0 .. max 
using the range function.

the function should 
add each nunber to a variable called sum

when the for statement executes 
and comes across the 'stop' number, 
the function should immediately 
add this value to sum 
and return the sum
'''

def loop(max, stop):
    summation = 0
    for num in range(max):
        summation += num
        if num == stop:
            return summation
    return summation

print(loop(10, 4) == 10)
print(loop(5, 5) == 10)
print("---")
print("---")
print("---")

'''
Problem 7:
Write a function number_of_coins(price) that:
returns the minimum number of coins 
someone will receive 
when making change for $1

for example, if the price is 27 cents, 
the amount of change will be 73 cents
2 quarters, 2 dimes, 3 pennies = 7 coins change

assume only quarters, dimes, nickels and pennies 
as your coins
'''

def number_of_coins(price):
    change = 100 - price
    coins = 0

    coins += change // 25
    change %= 25

    coins += change // 10
    change %= 10

    coins += change // 5
    change %= 5

    coins += change // 1
    change %= 1

    return coins

print(number_of_coins(27) == 7)
print(number_of_coins(99) == 1)
print(number_of_coins(100) == 0)
print("---")
print("---")
print("---")

'''
Problem 8

Write a function is_pythagorean_triple(s1, s2, s3)
return true 
if the three sides of a right triangle 
are valid Pythagorean triples

to be a Pythagorean triple 
the three sides must satisfy the relationship 
that the sum of the squares of two sides 
is equal to the square of the hypotenuse.

def is_pythagorean_triple(s1, s2, s3):
    sides = [s1, s2, s3]
    return max(s1, s2, s3) ** 2 == sum([side ** 2 for side in sides if side != max(s1, s2, s3)])
'''

def is_pythagorean_triple(s1, s2, s3):
    sides = [s1, s2, s3]
    hypotenuse = max(s1, s2, s3)

    # legs = [s for s in sides if s != hypotenuse]
    legs = filter(lambda s: s != hypotenuse, sides)

    # legs_sqaure = [leg ** 2 for leg in legs]
    legs_sqaure = map(lambda leg: leg ** 2, legs)

    if hypotenuse ** 2 == sum(legs_sqaure):
        return True

    return False

print(is_pythagorean_triple(3, 4, 5) == True)
print(is_pythagorean_triple(13, 4, 8) == False)
print(is_pythagorean_triple(15, 9, 12) == True)
print("---")
print("---")
print("---")

'''
Problem 9:

Write a function compute_grade(score) based on:
if the score is greater than or equal to 150, 
    return 'A'
if the score is between 100 - 149, 
    return 'B'
if the score is less than 100 
    return 'F'
'''

def compute_grade(score):
    if score >= 150:
        return 'A'
    if score >= 100 and score <= 149:
        return 'B'
    return 'F'

print(compute_grade(199) == 'A')
print(compute_grade(125) == 'B')
print(compute_grade(10) == 'F')
print("---")
print("---")
print("---")


'''
Problem 10:
Write a function my_mean(my_list) 
that computes the mean 
of a list of values 
using the statistics module
'''

def my_mean(my_list):
    return stats.mean(my_list)

print(my_mean([2,3,4,5]) == 3.5)
print(my_mean([99,122,765,9876]) == 2715.5)
print("---")
print("---")
print("---")
