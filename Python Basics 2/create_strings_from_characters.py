'''create_strings_from_characters'''


def create_strings_from_characters(frequencies, string1, string2):
    '''create_strings_from_characters'''
    final_score = 0
    score = 0

    for char in set(string1):
        if char in frequencies:
            current_char_count = string1.count(char)
            if frequencies.get(char,0) >= current_char_count:
                update_char_count = frequencies.get(char,0) - current_char_count
                frequencies.update({char: update_char_count})
                score += 1

    if score == len(string1):
        final_score += 1

    score = 0

    for char in set(string2):
        if char in frequencies:
            current_char_count = string2.count(char)
            if frequencies.get(char,0) >= current_char_count:
                update_char_count = frequencies.get(char,0) - current_char_count
                frequencies.update({char: update_char_count})
                score += 1

    if score == len(string2):
        final_score += 1

    return final_score


FREQUENCIES = {
    "h": 2,
    "e": 1,
    "l": 1,
    "r": 4,
    "a": 3,
    "o": 2,
    "d": 1,
    "w": 1
}

STRING1 = "hello"
STRING2 = "world"

print(create_strings_from_characters(FREQUENCIES, STRING1, STRING2))

# Copyright © 2022 AlgoExpert LLC. All rights reserved.

def create_strings_from_characters2(frequencies, string1, string2):
    can_create_string1 = can_create_string_from_frequencies(
        frequencies, string1)
    can_create_string2 = can_create_string_from_frequencies(
        frequencies, string2)

    if (not can_create_string1) or (not can_create_string2):
        if can_create_string1 or can_create_string2:
            return 1

        return 0

    for character in string1 + string2:
        if character not in frequencies or frequencies[character] == 0:
            return 1

        frequencies[character] -= 1

    return 2


def can_create_string_from_frequencies(frequencies, string):
    for character in set(string):
        if string.count(character) > frequencies.get(character, 0):
            return False

    return True