'''file_name'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
from collections import Counter
print(" ")

student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

# Accessing keys, values, and items
keys = student.keys()
print(keys)

values = student.values()
print(values)

items = student.items()
print(items)


# Getting value for a specific key
name = student.get("name")
print(name)

# Removing a key-value pair
grade = student.pop("grade")
print(items)

# Updating the dictionary
student.update({"age": 21, "grade": "B"})
print(items)

# Iterating over the view objects
for key in student.keys():
    print(key)

# Changes are reflected in the view objects
for value in student.values():
    print(value)  # Updated value is printed

# Converting view object to a list or tuple
keys_list = list(keys)
print(keys_list)
values_tuple = tuple(values)
print(values_tuple)

# Clearing the dictionary
student.clear()
print(items)
print()
print()

"""Using a dictionary to represent an instructor's grade book."""
grade_book = {            
    'Susan': [92, 85, 100], 
    'Eduardo': [83, 95, 79],
    'Azizi': [91, 89, 82],  
    'Pantipa': [97, 91, 92] 
}

all_grades_total = 0
all_grades_count = 0

for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f}')
    all_grades_total += total
    all_grades_count += len(grades)

print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")

print()
print()

"""Tokenizing a string and counting unique words."""

text = ('this is sample text with several words '
        'this is more sample text with some different words')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))
print()
print()

text = ('this is sample text with several words '
        'this is more sample text with some different words')
counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')
print('Number of unique keys:', len(counter.keys()))

print()
days_per_month = {'January': 31, 'February': 28, 'March': 31}
print()
str1 = 'abcd'
print(':'.join(str1))