'''
print(" ")
'''
print(" ")

def remove_chars(base, chars=""):
    '''
    remove_chars
    '''
    new_string = base
    for char in chars:
        new_string = new_string.replace(char, "")

    return new_string


RESULT = remove_chars("Hello World", "l")
print(RESULT)
print(" ")


def sum_list(lst):
    '''
    sum_list
    '''

    total = 0
    for num in lst:
        total += num
    return total


def sum_lists(list1, list2):
    '''
    sum_lists
    '''
    total = 0
    total += sum_list(list1)
    total += sum_list(list2)
    return total


SUM_RESULT = sum_lists([1, 22, 3], [88, 44, 33])
print(SUM_RESULT)

print(" ")


def string_lengths(strings):
    '''
    string_lengths
    '''

    lengths = []

    for string in strings:
        length = len(string)
        lengths.append(length)

    return lengths


def compare_lists(lst1=[], lst2=[]):
    '''
    compare_lists
    '''
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    set_intersection = lst1_set.intersection(lst2_set)

    return len(set_intersection)


def trim_list(lst, elements_to_trim):
    '''
    trim_list
    '''

    trimmed_list = []

    for idx in range(len(lst) - elements_to_trim):
        element = lst[idx]
        trimmed_list.append(element)

    return trimmed_list


def running_sums(numbers):
    '''
    running_sums
    '''

    sums = []
    current_sum = 0

    for number in numbers:
        current_sum += number
        sums.append(current_sum)

    return sums