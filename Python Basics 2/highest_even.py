'''highest_even.py'''
print(" ")


def highest_even(lst):
    '''highest_even'''
    highest_even_number = lst[0]

    for num in lst:
        if num > highest_even_number and num % 2 == 0:
            highest_even_number = num

    return highest_even_number


nums = [10, 2, 3, 4, 5, 11]
print(highest_even(nums))
print(" ")
