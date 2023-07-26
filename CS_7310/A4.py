'''assignment 4'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
import re
import csv
import json

print(" ")

'''

Problem 1
Write a function is_ok_phone_number(str):

must begin with ONLY area codes: 212, 718

separator can be either period (.) or dash(-) 
but not mixed

example: 212.987.2123, 718-222-3365
'''

#  Write code

def correct_area_code(string):
    correct_area_codes = ['212', '718']
    area_code = string[:3]
    return area_code in correct_area_codes

def mixed_separator(string):
    period_count = string.count('.')
    dash_count = string.count('-')
    return period_count >= 1 and dash_count >= 1

def is_ok_phone_number(str):
    if not correct_area_code(str):
        return False
    if mixed_separator(str):
        return False
    return True


# Assertions
print(is_ok_phone_number('212.207.8876') == True)
print(is_ok_phone_number('212.207-8876') == False)
print(is_ok_phone_number('718.207.8876') == True)
print(is_ok_phone_number('912.207.8876') == False)
print(is_ok_phone_number('212-207-8876') == True)
print("---")
print("---")
print("---")


'''
Problem 2:
write a function test_str1(s)
that uses regex to test for a match

You have a string s

return True if: 
-- it begins with a digit. 
-- ends with a period (.) symbol. 
-- contains only word characters
between the start and end of teh string 
-- the length of the string is 6 characters long only.

False otherwise
'''

# function
def test_str1(s):
    pattern = r"^(\d)(\w{4})(\.$)"
    match = re.search(pattern, s)
    return bool(match)

print(test_str1('6qwer.') == True)
print(test_str1('6qwer,') == False)
print(test_str1('6qweer.') == False)
print(test_str1('6q&er.') == False)
print(test_str1('Aqwer.') == False)
print("---")
print("---")
print("---")


'''
Problem 3:
Write a function test_str2(s):
return True if
-- the string begins with any of the letters a-g 
-- the second character is a number in the range 3-6 
-- the third character may be any character 
-- the fourth chracter may be anything except A or B or C

return False otherwise
'''

# 3 code
def test_str2(s):
    pattern = r'^[a-g][3-6].[^ABC]$'
    match = re.search(pattern, s)
    return bool(match)


print(test_str2('a6&y') == True)
print(test_str2('a6&yd') == False)
print(test_str2('96&y') == False)
print("---")
print("---")
print("---")


'''
Problem 4
write a function test_str4(s): 
-- uses regex

-- s must be length 10

-- The first 5 characters should consist of letters
(both lowercase and uppercase),
or of even digits.

-- The last 5 characters should consist of
odd digits 
or whitespace characters.
'''


def test_str4(s):
    pattern = r'^([a-zA-Z2468]{5})([13579\s]{5})$'
    match = re.search(pattern, s)
    return bool(match)


print(test_str4("aaa6413511") == True)
print(test_str4("aaa64135  ") == True)
print(test_str4("aaa641351\t") == True)
print(test_str4("aaa64135117") == False)
print("---")
print("---")
print("---")


'''
Problem 5:
write a function test_str5(s):
Using regex tests that a string
must start with Mr., Mrs., Ms., or Dr.
followed by a one or more space characters
followed by a name

The name must begin with an uppercase letter
followed by any number of lowercase letters
return True or False
'''


def test_str5(s):
    pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.)(\s+)([A-Z])([a-z]*$)'
    match = re.search(pattern, s)
    return bool(match)


print(test_str5("Dr. Jones") == True)
print(test_str5("Dr.\t\tJones") == True)
print(test_str5("Ms. JJnes") == False)
print(test_str5("Mrs Smyths") == False)
print("---")
print("---")
print("---")


'''
Problem 6:
Your task is to write a function test_str6(s)
you are given a string with multiple sentences
(end in .). 

For each sentence that contains with the phrase: 
-- someone1 knows someone2

-- where there may be multiple spaces
before and after the word 'knows'

-- use regex groups 
to add someone1 to a list of subjects 

-- use regex groups
to add someone2 to a list of objects 

-- return both
the list of subjects
and the list of objects
'''

# function definition
# x likes z  - return subjects and objcts


def test_str6(big_s):
    sentences = big_s.split('.')
    subjects = []
    objects = []
    for sentence in sentences:
        pattern = r'(^\s*)(\w*)(\s*)(knows)(\s*)(\w*)'
        match = re.search(pattern, sentence)
        if bool(match):
            subjects.append(match[2])
            objects.append(match[6])
    return subjects, objects


# asserts
big_str = "joe knows bob. ed    knows    marie. zz xx cc"
slist, olist = test_str6(big_str)

print(test_str6(big_str) == (['joe', 'ed'], ['bob', 'marie']))
print("---")
print("---")
print("---")


'''
Problem 7:
Write a function : get_html_tag_names(s):

return a set
of all the html tags in the string

html elements are written between 2 tags 
: ....text ...
'''

# function definition
def get_html_tag_names(s):
    html_tags = set()
    pattern = r'<([^/\s>]+)'
    matches = re.findall(pattern, s)
    for match in matches:
        html_tags.add(match)
    return html_tags


# asserts
s = '''
    <p><a href='http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p><div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>
    '''
tag_set = get_html_tag_names(s)
print(tag_set == {'p', 'a', 'div'})
print("---")
print("---")
print("---")


'''
Problem 8:
Write a function : is_ip_address(s):
return True
if the s is an IPv4 or IPV5 address,
False otherwise 

IPv4 was the first publicly used Internet Protocol
which used 4 byte addresses
which permitted for 232 addresses.

The typical format of an IPv4 address
is A.B.C.D 
where A, B, C and D are Integers
lying between 0 and 255 (both inclusive).

IPv6, with 128 bits
was developed to permit
the expansion of the address space.

To quote from the linked article:
The 128 bits of an IPv6 address
are represented in 8 groups of 16 bits each.

Each group is written as
4 hexadecimal lowercase digits
and the groups are separated by colons (:).

The address 2001:0db8:0000:0000:0000:ff00:0042:8329
is an example of this representation.
'''


def is_IPv4(s):
    IP_address = s.split('.')
    pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    for num in IP_address:
        if not re.match(pattern, num):
            return False
    return True

def is_IPv6(s):
    IP_address = s.split(':')
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    for group in IP_address:
        if not re.match(pattern, group):
            return False
    return True

# code #8
def is_ip_address(s):
    return (is_IPv4(s) or is_IPv6(s))

# assert
print(is_ip_address("120.08.9.255") == True)
print(is_ip_address("120.08.9.265") == False)
print(is_ip_address("120.08.9.255.20") == False)
print(is_ip_address("A.08.9.25") == False)
print("Pass IPV4")
print(is_ip_address("2001:0db8:0000:0000:0000:ff00:0042:8329:2123") == False)
print(is_ip_address("2001:0db8:0000:0000:0000:ff00:0042:8329") == True)
print(is_ip_address("2001:0dm8:0000:0000:0000:ff00:0042:8329") == False)
print(is_ip_address("2001:0db8:0000:0000:0000:ff00:042:8329") == False)
print("Pass IPV6")
print("---")
print("---")
print("---")


'''
Problem 9
Write a function: gen_dict_from_file(filename) :
that reads a text file
and returns a dictionary

where the keys 
are the words in the file
and the value
is the number of times the word appears in the file.

note: 
a word is defined by the regex definition for \w+
'''


def gen_dict_from_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            pattern = r'\w+'
            word_list = re.findall(pattern, text)
            word_set = set(re.findall(pattern, text))
            word_count = {}
            for word in word_set:
                word_count[word] = word_list.count(word)
            return word_count

    except FileNotFoundError:
        print('The file name you specified does not exist')


# assert
print(gen_dict_from_file('a4q9.txt') == {
      'rollo': 3, 'ate': 1, 'pizza': 4, 'a': 1, 'with': 2, 'anchovies': 2, 'likes': 2, '22': 1})
print("---")
print("---")
print("---")

'''
Problem 10
write a function count_lines(filename)
return the number of lines in the file
a line is a sequence of characters
followed by a newline \n
'''

# code


def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            pattern = r'\n'
            match = re.findall(pattern, text)
            return len(match)

    except FileNotFoundError:
        print('The file name you specified does not exist')

# assert


print(count_lines('a4q10.txt') == 5)
print("---")
print("---")
print("---")

'''
Problem 11
write a function read_json(filename):
the file contains json of the form: 
{
    'accounts': [
        {'account': 100, 'name': 'Jones', 'balance': 24},
        {'account': 200, 'name': 'Doe', 'balance': 345}
    ]
}

read the json into a python data structure
and return the sum of all the balances
'''
# code

def read_json(fname):
    try:
        with open(fname, 'r') as file:
            data = json.load(file)
            accounts_sum = 0
            for account in data['accounts']:
                accounts_sum += int(account['balance'])
            return accounts_sum
    except FileNotFoundError:
        print('The file name you specified does not exist')

# assert
print(read_json('a4q11.json') == 369)
print("---")
print("---")
print("---")


'''
Problem 12
write a function read_csv_get_amount(filename):
the file contains csv that
may or may not contain a field called amount

if the file contains an amount field,
return the sum of all the amounts

if the file does not contain a field called amount,
return None

note: 
the position of amount
in the csv file
may vary
'''

#code
def get_col_num(reader, field):
    col_num = 0
    for row in reader:
        for col in row:
            if col == field:
                return col_num
            col_num += 1
    return -1

def read_csv_get_amount(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            col_num = get_col_num(reader, 'amount')
            if col_num == -1:
                return None

            amount_sum = 0
            for row in reader:
                amount_sum += int(row[col_num])
            return amount_sum

    except FileNotFoundError:
        print('The file name you specified does not exist')

#assert #12
print(read_csv_get_amount('a4q12.csv')  == 1500)
print(read_csv_get_amount('a4q12b.csv')  == 1554)
print(read_csv_get_amount('a4q12c.csv')  == None)
print("---")
print("---")
print("---")



'''
Problem 13
write a function catch_div_zero(v1, v2):
the code provided
returns the result of dividing v1 by v2

However,
the code will throw Exception/Errors if 
-- division by zero occurs,
or -- a non-numeric value is passed as a parameter

your task is to use a 
try..except block 
to catch a ZeroDivisionError or a TypeError

and return the either the string
'ZeroDiv' or 'TypeError'

If no exception,
then return the result of the division
'''

#code
def catch_div_zero(v1, v2):
    try:
        return v1 / v2
    except TypeError:
        return 'TypeError'
    except ZeroDivisionError:
        return 'ZeroDiv'

# assert
print(catch_div_zero(4, 2) == 2.0)
print(catch_div_zero(4, 0) == 'ZeroDiv')
print(catch_div_zero(4, '9') == "TypeError")
print("---")
print("---")
print("---")
