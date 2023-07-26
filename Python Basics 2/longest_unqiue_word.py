'''longest_unqiue_word'''
print(" ")

# Copyright © 2022 AlgoExpert LLC. All rights reserved.


def get_n_longest_unique_words(words, n):
    '''get_n_longest_unique_words'''
    unique_words = get_unique_words(words)
    #sorted_words = sorted(unique_words, key=len, reverse=True)
    #return sorted_words[:n]
    longest_words = []

    while len(longest_words) < n:
        current_longest = ""
        for word in unique_words:
            if len(word) > len(current_longest):
                current_longest = word

        unique_words.remove(current_longest)
        longest_words.append(current_longest)

    return longest_words


def get_unique_words(words):
    '''get_unique_words'''
    unique_words = []
    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)

    return unique_words


word_list = [
    "Longer",
    "Whatever",
    "Longer",
    "Ball",
    "Rock",
    "Rocky",
    "Rocky"
]

print(get_n_longest_unique_words(word_list, 3))
print(" ")
