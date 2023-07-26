'''assignment 2'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
from random import randint, shuffle


print(" ")

'''
For each problem you need to write code for a function based on the requirements.
The function initally only contains the code 'pass' which does nothing
Your task is to write correct code that follows the coding guidelines.
In the cell following the code cell, the assertion statements that will test your code.
If there is an error, the assertion will throw an Error.
If you pass all the assertions, you will see the print statement display 'Passed'
'''

'''
Problem 1
Write a function sum_all(n) that 
calculates the sum of all numbers 
from 1 to a given number n, 
including n
'''

def sum_all(n):
    summation = 0
    for num in range(1, n+1):
        summation += num
    return summation

print(sum_all(10) == 55)
print(sum_all(1) == 1)
print("---")
print("---")
print("---")

'''
Problem 2
Write code for a function that 
returns True if n is a prime number, 
False otherwise.

A Prime Number is a number 
that cannot be made 
by multiplying other whole numbers.

A prime number is a natural number 
greater than 1 
that is not a product 
of two smaller natural numbers
'''

def is_prime(n):
    if n <= 1:
        return False

    if not isinstance(n, int):
        return False

    if n % 1 != 0:
        return False

    for num in range(2, n):
        if n % num == 0:
            return False

    return True

print(is_prime(37) == True)
print(is_prime(47) == True)
print(is_prime(100) == False)
print("---")
print("---")
print("---")

'''
Problem 3
Write code for a function sum_primes(n) 
that returns sum of all the prime numbers p 
such that 0 < p < n

Use a for loop 
and 
your function from problem 2
'''

def sum_primes(n):
    summation = 0
    for num in range(2, n):
        if is_prime(num):
            summation += num
    return summation

print(sum_primes(20) == 77)
print(sum_primes(31) == 129)
print("---")
print("---")
print("---")

'''
Problem 4
Write code in ONE line for a function sum_primes2(n)
returns sum of all the prime numbers p such that 0 < p < n
use your is_prime() code from problem 2
HINT: Use a list comprehension 
to get this done in one line of code 
inside your function
'''
def sum_primes2(n):
    return sum([num for num in range(2, n) if is_prime(num)])

print(sum_primes2(20) == 77)
print(sum_primes2(31) == 129)
print("---")
print("---")
print("---")


'''
Problem 5:
write a function is_perfect_square(n) that:
returns True if n is a perfect square, 
False otherwise

a perfect square is a number 
that is 
the product of the same 2 integers

example perfect squares: 
-- 4 = 2 * 2
-- 16 = 4 * 4
'''

def is_perfect_square(n):
    for num in range(n):
        if num * num == n:
            return True
    return False

print(is_perfect_square(4) == True)
print(is_perfect_square(16) == True)
print(is_perfect_square(100) == True)
print(is_perfect_square(101) == False)
print("---")
print("---")
print("---")


'''
Problem 6
The famous Fibonacci sequence 
is one where 
each number 
is the sum of the previous 2 numbers

(starting with 0, 1) as in: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..-

An interesting property of a fibonacci number
is that 
a number n is fibonacci 
if and only if one or both of: 
(5n^2 + 4) 
or 
(5n^2 - 4) 
is a PERFECT SQUARE (Problem 5!)

write a boolean function is_fibo(n) 
that returns True 
if n is a fibonacci number, 
False otherwise 

-- use your is_perfect_square function (Problem 5)

def is_fibo(n):
    seq = (0, 1)
    for num in range(1, n):
        if num == seq[-1] + seq[-2]:
            seq = (seq[-1], num)
    return n == seq[-1] + seq[-2]
'''

def is_fibo(n):
    return is_perfect_square(5 * n**2 + 4) or is_perfect_square(5 * n**2 - 4)

print(is_fibo(5) == True)
print(is_fibo(21) == True)
print(is_fibo(55) == True)
print(is_fibo(33) == False)
print(is_fibo(100) == False)
print("---")
print("---")
print("---")

'''
Problem 7:
Write a function is_monotonic (my_list) that:
returns True if the list is monotonic increasing 
or 
returns True if the list is monotonic descreasing, 
False otherwise

a list is monotonic increasing 
if the sequence increases 
or stays the same: 
-- 2,3,5,6,6,7

a list is monotonic decreasing 
if the sequence decreases 
or stays the same: 
-- 9,8,8,7,4,2
'''

def is_montonic_increasing(my_list):
    last_num = my_list[0]
    for num in my_list:
        if num < last_num:
            return False
        last_num = num
    return True

def is_montonic_decreasing(my_list):
    last_num = my_list[0]
    for num in my_list:
        if num > last_num:
            return False
        last_num = num
    return True

def is_monotonic(my_list):
    return is_montonic_increasing(my_list) or is_montonic_decreasing(my_list)

print(is_monotonic([2,3,4,6,8]) == True)
print(is_monotonic([2,3,5,2,9]) == False)
print(is_monotonic([100,99,66, 44]) == True)
print(is_monotonic([100,99,66, 88]) == False)
print("---")
print("---")
print("---")


'''
Problem 8:
Write a function calc_2(a, b):
return two values
the first value should be the sum of a and b
the second value: a - b
'''

def calc_2(a,b):
    return a + b, a - b

print(calc_2(10, 2) == (12, 8))
print(calc_2(-10, 2) == (-8, -12))
print("---")
print("---")
print("---")


'''
Problem 9:
Write a function average_of_digits(str) based on:
return the average 
of all the digits 
contained in the string str
'''

def average_of_digits(str):
    digits = [int(char) for char in str if char.isdigit()]
    if len(digits) == 0:
        return 0
    return sum(digits) / len(digits)

print(average_of_digits('a399z') == 7)
print(average_of_digits('abc') == 0)
print(average_of_digits('a2b2c2') == 2)
print("---")
print("---")
print("---")


'''
Problem 10:
Write a function new_string(s1, s2) that 
returns a string 
that consists of s1 and s2's 
first, middle and last characters.

if either s1 or s2 
has an even number of characters, 
return None
'''

def new_string(s1, s2):
    if len(s1) % 2 == 0 or len(s2) % 2 == 0:
        return None
    string = str(s1[0] + s2[0])
    string += s1[(len(s1) // 2)] + s2[(len(s2) // 2)]
    string += s1[-1] + s2[-1]
    return string

print(new_string('AbC', 'DeF') == 'ADbeCF')
print(new_string('Apple', 'BanjoFret') == 'ABpoet')
print(new_string('AbC', 'DeFt') == None)
print("---")
print("---")
print("---")


'''
Problem 11
Write a function message_from_two_lists(list1, list2)
that creates a string 
where the first elements
of list1 and list2 
are concatenated 
and followed by a space.

Continue for each element of the list. 
If one list has more elements
than the other list, 
ignore extra elements.

The string you return 
should not end 
in a space character

def message_from_two_lists(list1, list2):
    string = ''
    idx = 0
    while idx < len(list1) and idx < len(list2):
        string += list1[idx] + list2[idx]
    return string
'''

def message_from_two_lists(list1, list2):
    message = []
    for str1, str2 in zip(list1, list2):
        message.append(str1 + str2 + ' ')
    return ''.join(message).rstrip()

print(message_from_two_lists(["Ho", 'sp', 'eter'], ['pe', 'rings', 'nal']) == "Hope springs eternal")
print(message_from_two_lists(['Py', 'inv', 'b', 'Gu', 'Ross'], ['thon', 'ented', 'y', 'ido']) == "Python invented by Guido")
print("---")
print("---")
print("---")


'''
Problem 12
Write a function remove(val, list) that 
removes all occurrences of val 
from a list 
and returns a list without any vals

def remove(val, lst):
    return list(filter(lambda num: num != val, lst))
'''

def remove(val, list):
    return [num for num in list if num != val]

print(remove(4, [1,2,3,4,5,4,7,4]) == [1,2,3,5,7])
print(remove(2, [4,2,5,6,2,2]) == [4,5,6])
print(remove(9, [4,2,5,6,2,2]) == [4,2,5,6,2,2])
print("---")
print("---")
print("---")


'''
Problem 13
Write a function add_to_list_in_tuple(val, tuple) that 
finds the first list
inside a tuple 
and modifies the first value
of that list 
to val

if there is no list contained
in the tuple, 
return the tuple
'''

def add_to_list_in_tuple(val, tuple):
    for ele in tuple:
        if isinstance(ele, list):
            ele[0] = val
            break
    return tuple

print(add_to_list_in_tuple(99, (8, 'foo', [1,2,3], 12.44)) == (8, 'foo', [99,2,3], 12.44))
print(add_to_list_in_tuple(99, (8, 'foo', (1,2,3), 12.44)) == (8, 'foo', (1,2,3), 12.44))
print("---")
print("---")
print("---")

'''
Problem 14
Write a function all_same(tuple) that 
returns True
if all the items
in a tuple
are the same,
False otherwise

if the tuple
is empty,
return None
'''

def all_same(tuple):
    if len(tuple) == 0:
        return None
    same_item = tuple[0]
    for item in tuple:
        if item != same_item:
            return False
    return True

print(all_same((2,2,2,2)) == True)
print(all_same((2,2,2,2,99)) == False)
print(all_same(([1,2,3], [1,2,3])) == True)
print(all_same(([1,2,3], [1,2,3], [1,2])) == False)
print(all_same(()) == None)
print(all_same((66,)) == True)
print("---")
print("---")
print("---")

'''
Problem 15
Write a function gen_pwd( ) that returns a password:
at least 10 characters
at least 1 uppercase letter
at least 2 different special characters in ($, *, #, @)
at least 1 digit

the order of the different character classes
should change 
with each call to gen_pwd(). 
-- this means uupercase should not always be followed by special chars followed by digits

the length of the password
should not be fixed
at one length -- mix it up! 

hackers can find your password patterns
and break your codes
'''

def gen_random_lowercase_char():
    return chr(ord('a') + randint(0, 25))

def gen_random_uppercase_char():
    return chr(ord('A') + randint(0, 25))

def gen_random_special_char():
    diff_special_chars = {
        1: '$',
        2: '*',
        3: '#',
        4: '@'
    }
    return diff_special_chars[randint(1, 4)]

def gen_pwd():
    password = []

    # Randomize the password length between 10 and 15
    password_length = randint(10, 15)

    # Generate random characters for each required class
    for _ in range(password_length):
        password.append(gen_random_lowercase_char())
        password.append(gen_random_uppercase_char())
        password.append(gen_random_special_char())
        password.append(gen_random_special_char())
        password.append(str(randint(0, 9)))

    shuffle(password)

    return ''.join(password)

def is_legal_pwd(s):
    # At least 10 characters, at least 1 uppercase letter
    # At least 2 different special characters in ($, *, #, @)
    # At least 1 digit

    if len(s) < 10:
        return False
    if len([c for c in s if c.isupper()]) == 0:
        return False
    if len([d for d in s if d.isdigit()]) < 1:
        return False
    if len([z for z in s if z in '$*#@']) < 2:
        return False
    return True

p1 = gen_pwd()
p2 = gen_pwd()
p3 = gen_pwd()

print(f"Generated passwords: p1={p1} p2={p2} p3={p3}")
print(is_legal_pwd(p1) == True)
print(is_legal_pwd(p2) == True)
print(is_legal_pwd(p3) == True)
print(p1 != p2)
print(len(set([len(p1), len(p2), len(p3)])) > 1)
