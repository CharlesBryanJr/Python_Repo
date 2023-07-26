# 7311 Coding Assignment 2

# write code for the following functions.
# note: these functions use the non-binding type hints feature new in Python 3.5
# It's good to get in the habit of writing your code this way

# All these functions return None so that the code compiles.
# Your job is to write code that returns a correct implementation of the function.

def get_longest_word(instring: str) -> str:
    '''
    do: Return the longest word in the instring.
    A word is a colelction of alphanumeric characters separated by one or more spoces.

    example: get_longest_word("jump holler  have a fabulous time" ) -> "fabulous"
    :param instring: string with space delimited words
    :return:  the longest wrord string
    '''

    return None

def count_char_frequency(instr : str) -> dict:
    '''
    do: extract each character in instr and use a dict to keep track of the number of occurrences
        of each character
    example: "abba"  -> {'a':2, 'b':2}
    :param instr: string of characters
    :return: dictionary
    '''

    return None

class MyVehicleClass:
    '''Add attributes number_wheels and weight.
       Add a method weight_per_wheel that returns weight/number_wheels
    '''
    pass

def test_vehicle_class (some_vehicle: object) -> float:
    '''

    :param some_vehicle: an instance of the MyVehicleClass
    :return: the value returned by the weight_per_wheel method
    '''

    return None


def regex_test (instring: str) -> list:
    import re
    '''
    do: write a regex string as a local variable to find 
        floating point numbers that have at least one digit preceding the decimal
        and at least two numbers following the decimal
    example: regex_test ("abc 2.987  44.8  999.99") -> ['2.987', '999.99']
    
    suggest: use the website http://regexpal.com  to test out regexes
    
    :param instring:   string to search for matches to regex
    :return:  list of matches
    '''

    regex_pattern  = r'your regex goes here'

    return re.findall(regex_pattern, instring)




print (f"get_long_word('bob found ridiculous book on shelf'):{get_longest_word('bob found ridiculous book on shelf')}")
print (f"count_char_frequency('abxgttyavb') : {count_char_frequency('abxgttyavb') }")

# OOP: create an instance of  MyVehicleClass called my_truck
# with number_wheels = 18 and weight = 500000
# pass my_truck to the test_vehicle_class function

my_truck = None   # modify this  creating an instance of MyVehicleClass


print(f"test_vehicle_class (my_truck): {test_vehicle_class (my_truck)}")

print (f"regex_test ('abc 2.987  44.8  999.99') : {regex_test ('abc 2.987  44.8  999.99')}")

