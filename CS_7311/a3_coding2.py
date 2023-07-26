# 7311 Coding Assignment 2

# write code for the following functions.
# note: these functions use the non-binding type hints feature new in Python 3.5
# It's good to get in the habit of writing your code this way

# All these functions return None so that the code compiles.
# Your job is to write code that returns a correct implementation of the function.
import pytest
import re

def get_longest_word(instring: str) -> str:
    '''
    do: Return the longest word in the instring.
    A word is a colelction of alphanumeric characters separated by one or more spoces.

    example: get_longest_word("jump holler  have a fabulous time" ) -> "fabulous"
    :param instring: string with space delimited words
    :return:  the longest wrord string
    '''
    words = instring.split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def count_char_frequency(instr : str) -> dict:
    '''
    do: extract each character in instr and use a dict to keep track of the number of occurrences
        of each character
    example: "abba"  -> {'a':2, 'b':2}
    :param instr: string of characters
    :return: dictionary
    '''
    char_count = {}
    for char in instr:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

class MyVehicleClass:
    '''Add attributes number_wheels and weight.
       Add a method weight_per_wheel that returns weight/number_wheels
    '''

    def __init__(self, number_wheels, weight):
        self.number_wheels = number_wheels
        self.weight = weight

    def weight_per_wheel(self):
        return self.weight / self.number_wheels

@pytest.fixture
def some_vehicle():
    '''
    Fixture to create an instance of MyVehicleClass for testing.
    '''
    return MyVehicleClass(18, 500000)

def test_vehicle_class (some_vehicle: MyVehicleClass) -> float:
    '''
    :param some_vehicle: an instance of the MyVehicleClass
    :return: the value returned by the weight_per_wheel method
    '''
    return some_vehicle.weight_per_wheel()


def regex_test(instring: str) -> list:
    '''
    do: write a regex string as a local variable to find
        floating point numbers that have at least one digit preceding the decimal
        and at least two numbers following the decimal

    example: regex_test ("abc 2.987  44.8  999.99") -> ['2.987', '999.99']
    suggest: use the website http://regexpal.com to test out regexes

    :param instring: string to search for matches to regex
    :return: list of matches
    '''

    regex_pattern = r'\d+\.\d{2,}'
    return re.findall(regex_pattern, instring)

print (f"get_long_word('bob found ridiculous book on shelf'):{get_longest_word('bob found ridiculous book on shelf')}")

print (f"count_char_frequency('abxgttyavb') : {count_char_frequency('abxgttyavb') }")

# OOP: create an instance of MyVehicleClass called my_truck
# with number_wheels = 18 and weight = 500000
# pass my_truck to the test_vehicle_class function

my_truck = MyVehicleClass(18, 500000)

print(f"test_vehicle_class(my_truck): {test_vehicle_class(my_truck)}")

print (f"regex_test ('abc 2.987  44.8  999.99') : {regex_test ('abc 2.987  44.8  999.99')}")