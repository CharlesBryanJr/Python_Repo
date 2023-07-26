'''assignment 3'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
from collections import Counter
import re

print(" ")

'''
Problem 1
Write a function gen_dict_from_lists(list1, list2)
return a dictionary
such that items from list1 are the keys
and items from list2 are the values
'''

def gen_dict_from_lists(list1, list2) :
    new_dict = {}
    for key, item in zip(list1, list2):
        new_dict[key] = item
    return new_dict

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(gen_dict_from_lists(keys, values) == {'Ten': 10, 'Twenty': 20, 'Thirty': 30})
print("---")
print("---")
print("---")

'''
Problem 2:
Write code for a function gen_new_dict(key_list, val_list):
that generates a dict based on two lists:
first parameter - list contains a list of keys
second paramteter - list of value

if the length of the two parameter lists are unequal,
return None
'''

def gen_new_dict(key_list, val_list):
    if len(key_list) != len(val_list):
        return None
    new_dict = {}
    for key, item in zip(key_list, val_list):
        new_dict[key] = item
    return new_dict

val_list = [10,20,30,40]
key_list = ['Moe', 'Willy', 'Curly', 'Larry']          
val_list2 = [11,22,33]

print(gen_new_dict(key_list, val_list) == {'Moe': 10, 'Willy': 20, 'Curly': 30, 'Larry': 40})
print(gen_new_dict(key_list, val_list2) == None)
print("---")
print("---")
print("---")


'''
Problem 3
Write a function gen_new_dict(dict1, person_salary_list):
generates a new dict
where the salary of persons
on the person_salary_list
updates valus in the original dictionary

example:
company_dict = {
  'emp1': {'name': 'Jack', 'salary': 7500},
  'emp2': {'name': 'Emma', 'salary': 8000},
  'emp3': {'name': 'Brad', 'salary': 500}
}
person_salary_list = [('Jack', 8800), ('Brad', 5000)]

NEW DICT
   
company_dict2 == {
    'emp1': {'name': 'Jack', 'salary': 8800},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 5000}
}
'''

def gen_new_dict_2(dict1, person_salary_list):
    new_dict = {key: value.copy() for key, value in dict1.items()}

    for person in person_salary_list:
        name, salary = person

        for employee_data in new_dict.values():
            if name == employee_data['name']:
                employee_data['salary'] = salary

    return new_dict

company_dict = {
    'emp1': {'name': 'Jack', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

person_salary_list = [('Jack', 8800), ('Brad', 5000)]

company_dict2 = gen_new_dict_2(company_dict, person_salary_list)

print(company_dict2 == {
    'emp1': {'name': 'Jack', 'salary': 8800},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 5000}
})
print(id(company_dict) != id(company_dict2))
print("---")
print("---")
print("---")


'''
Problem 4
Write a function get_min_value(dict1):
returns the key with the minimum value.
assume all values are integer
'''
def find_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key

def get_min_value(dict1):
    min_value = min([value for value in (x for x in dict1.values())])
    return find_key(dict1, min_value)


#4 assert

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'History': 75
}

print(get_min_value(sample_dict) == 'Math')
print("---")
print("---")
print("---")


'''
Problem 5:
write a function gen_dict(list1):
returns a dict
where the key
is a word in dict1 
and the value
is the number of times it appears in the list1 parameter

def gen_dict(list1):
    new_dict = {}
    for key in list1:
        if key in new_dict:
            continue
        new_dict[key] = list1.count(key)
    return new_dict
'''

def gen_dict(list1):
    return {key: list1.count(key) for key in list1}


# asserts
list1 = ['foo', 'bar', 'foo', 'zork', 'zork', 'zork']
print(gen_dict(list1)  == {'foo': 2, 'zork': 3, 'bar':1})
print("---")
print("---")
print("---")


'''
Problem 6:
Use the Counter class
to help generate a dict
that tracks the words
and the number of times seen in list1
'''

# function definition
def gen_dict_with_counter(list1):
    return dict(Counter(list1))

# asserts

list1 = ['foo', 'bar', 'foo', 'zork', 'zork', 'zork']
print(gen_dict_with_counter(list1)  == {'foo': 2, 'zork': 3, 'bar':1})
print("---")
print("---")
print("---")


'''
Problem 7:
Write a function word_list_of_most_unique_sentence(bigstr):
returns a list of the words
for the sentence in bigstr
with the most individual words.

a sentence is any collection of words
separated by a period (.)

example: 
'joe jumps over the hay' has 5 unique words 
'joe joe jumps jumps hay' has 3 unique words

note how the assert uses sets to compare lists for equality
'''

def word_list_of_most_unique_sentence(bigstr):
    most_unique_words = set()
    sentences = bigstr.split('. ')
    for sentence in sentences:
        words = re.split(r"[,.\s]+", sentence)
        unique_words = set(words)
        most_unique_words = max(unique_words, most_unique_words, key=len)
    return list(most_unique_words)

# asserts
bigstr =  "bob is very bob. go dog go, go dog go, go dog, go dog. zorro had excellent swordplay. love is love. me me me me me."

w_list = word_list_of_most_unique_sentence(bigstr)

print(isinstance(w_list, list) == True)
print(set(w_list) == set(['zorro', 'had', 'excellent', 'swordplay']))
print("---")
print("---")
print("---")



'''
Problem 8:
Write a function number_of_alpha_sentences(big_str):
return the number of sentences in big_str
that have only alphabetic characters and spaces.

the alphabetic characters may be upper or lower case
'''

#function definition
def number_of_alpha_sentences(big_str):
    alpha_sentences_count = 0
    sentences = big_str.split(".")
    for sentence in sentences:
        iterable = (x for x in sentence)
        if not any(char.isdigit() for char in iterable):
            alpha_sentences_count += 1
    return alpha_sentences_count - 1

# asserts

big_str = "Bob ate 9 pizzas. Zelda    called the doctor. The doctor said maybe he should go on TV. Zelda gave him 2 aspirin."
print(number_of_alpha_sentences(big_str) == 2)
print("---")
print("---")
print("---")

'''
Problem 9:
Write a function keep_odd_numbers(s):
returns a string
that contains only the odd numbers
in the string passed in as s
'''

# function definition
def keep_odd_numbers(s):
    odd_nums = ''
    for char in (x for x in s):
        if not char.isdigit():
            continue
        num = int(char)
        if num % 2 != 0:
            odd_nums += str(num)
    return odd_nums


#assert
print(keep_odd_numbers("abc1234567&&zzxcvcbc9")  == "13579")
print("---")
print("---")
print("---")

'''
Problem 10:
Write a function is_contained_in(s1, s2):
return True
if all the characters in s1 appear in s2
'''

# function definition
def is_contained_in(s1, s2):
    return set(s1) < set(s2)

#asserts 
print(is_contained_in('AbC', 'DeF') == False)
print(is_contained_in('Ap', 'Apple Computer') == True)
print(is_contained_in('Apx', 'Apple Computer') == False)
print("---")
print("---")
print("---")
