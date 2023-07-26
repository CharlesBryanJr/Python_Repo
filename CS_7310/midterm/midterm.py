# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0121
# pylint: disable=E0401
import numpy as np
import pandas as pd
import statistics
import csv
import matplotlib.pyplot as plt
import time

print()

'''
NumPy Measurement

Compare the performance
of the built-in function sum()
that sums all the values in a 2D NumPy array 
vs.
using two loops
to visit all the cells of the array
and iteratively adding the values.

Steps:
Use the numpy arange ( ) function
to create a 1D numpy array (call it arr1d)
of 100 million floating point numbers.
The array will contain 100_000_000 floating point numbers.

Convert the 1D array to a 2D array with 10 columns using:
ncols = 10
arr2d = np.reshape(arr1d, (-1, ncols))

Use the timing technique
shown in the NumPy module
to measure the time it takes NumPy
to compute the sum of all values in arr2d

Write a function called compute_sum(arr)
that takes a numpy 2d array as parameter
and uses two loop to iterate over all the values
in the rows and columns
and compute the sum
and return the sum

Hint: use the shape property of numpy arrays
to determine the number of rows and columns
Hint: use NumPy's arr[row, col]
to get the value in cells of the array
and compute the sum

Use the timing technique
to measure the time it takes
to compute the sum iteratively

Be sure to check
that the sum is the same
for both methods
'''
def compute_sum(arr):
    rows, columns = arr.shape

    if not isinstance(arr, np.ndarray) or arr.ndim != 2 or columns != 10:
        print("The array is not a 2D NumPy array with 10 columns.")
        return None

    summation = 0
    for row in range(rows):
        for col in range(columns):
            summation += arr[row, col]
    return summation

def compare_sums(sum1, sum2):
    if sum1 != sum2:
        print("Sums are not equal.")
        print(f"Sum1: {sum1}")
        print(f"Sum2: {sum2}")

def faster_time(time1, time2):
    if time1 < time2:
        print("sum() function is the winner")
        print(f"time1: {time1}")
        print(f"time2: {time2}")
        print(f"The sum() function is faster than computing the sum with loops by {time2 - time1} seconds.")
    else:
        print("Computing the sum with loops is the winner")
        print(f"time1: {time1}")
        print(f"time2: {time2}")
        print(f"The computing the sum with loops is faster than the sum() function by {time2 - time1} seconds.")


arr1d = np.arange(100_000_000).astype(float)
ncols = 10
arr2d = np.reshape(arr1d, (-1, ncols))

np_start_time = time.time()
np_sum = arr2d.sum()
np_end_time = time.time()
NumPy_sum_duration = np_end_time - np_start_time

iteration_start_time = time.time()
iteration_sum = compute_sum(arr2d)
iteration_end_time = time.time()
iteration_sum_duration = iteration_end_time - iteration_start_time

compare_sums(np_sum, iteration_sum)
faster_time(NumPy_sum_duration, iteration_sum_duration)

labels = ['NumPy Sum', 'Iteration Sum']
values = [NumPy_sum_duration, iteration_sum_duration]
plt.bar(labels, values)
plt.xlabel('Methods')
plt.ylabel('Time')
plt.title('Comparison of Time Durations')
plt.yscale('log')
for i, value in enumerate(values):
    plt.text(i, value, str(value), ha='center', va='bottom')
plt.show()
print()

'''
2. CSV Data Set Processing
Tip: review the section in the Deitel book
section 9.12.3 Reading the Titanic Disaster Dataset

Load the Titanic CSV dataset into a pandas DataFrame.

Determine the number of individuals
who died vs. those that survived

Plot these values
with a Bar Chart using pyplot

Determine the average age
of survivors vs. those who died

Plot these values
with a Bar Chart using pyplot
'''

try:
    data = pd.read_csv('titanic.csv')
except FileNotFoundError:
    print("FileNotFoundError")

deaths = len(data['Survived']) - data['Survived'].sum()
survivors = len(data['Survived']) - deaths

print(f'Deaths: {deaths}')
print(f'Survivors: {survivors}')

labels = ['Survivors', 'Deaths']
values = [survivors, deaths]
plt.bar(labels, values)
plt.xlabel('Result')
plt.ylabel('# of People')
for i, value in enumerate(values):
    plt.text(i, value, str(value), ha='center', va='bottom')
plt.show()

survivors_age = []
deaths_age = []

iterable = range(len(data['Survived']))
survivors_age = (data['Age'][idx] for idx in iterable if data['Survived'][idx])
deaths_age = (data['Age'][idx] for idx in iterable if not data['Survived'][idx])

survivors_avg_age = statistics.mean(survivors_age)
deaths_avg_age = statistics.mean(deaths_age)

print(f'Average age of Deaths: {deaths_avg_age}')
print(f'Average age of Survivors: {survivors_avg_age}')

labels = ['Survivors','Deaths']
values = [survivors_avg_age, deaths_avg_age]
plt.bar(labels, values)
plt.xlabel('Result')
plt.ylabel('Average age')
for i, value in enumerate(values):
    plt.text(i, value, str(value), ha='center', va='bottom')
plt.show()


print()

'''
Debugging 
Rollo wrote the following program
and needs your help

# Rollo's code:
def foo(n):
    sum = 0
    for idx in range(n):
        sum = sum + 0.01 * idx
    return sum

sum = foo(2000)

print(sum)

For some reason,
Rollo want to use a debugger
to set a conditional breakpoint
when the index variable idx
has a value of 99.

Use a conditional debugger
to stop the debugger
when idx has as value of 99
before idx gets added to the sum.

What is the value of
the sum
before idx (99) gets added? ____

Using the debugger STEP function
to step thru the loop,
what is the value of sum
AFTER 99 gets added to the sum? _____-
'''

# Rollo's code:
def foo(n):
    s = 0
    for idx in range(n):
        s1 = s + 0.01 * idx
    return s

sum = foo(2000)

print(sum)

print()
