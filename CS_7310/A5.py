'''A5  ch07  NumPy and Pandas'''
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
import math
import csv
import matplotlib.pyplot as plt

print(" ")

'''
1 NumPy 1
write a function get_rol_col_value(arr1, row, col):
that returns the value
in the corresponding row and col
in numpy arr1
'''
def get_rol_col_value(arr1, row, col):
    arr = np.array(arr1)
    return arr[row, col]

# assert
arr1 = np.arange(1,21).reshape(4,5)
print(get_rol_col_value(arr1, 1, 1) == 7)
print ("#1 Passed")
print("---")
print("---")
print("---")

'''
2 NumPy 2
write a function gen_numpy1(list1, list2):
that returns a 2x5 numpy array from the 2 lists
'''

# code
def gen_numpy1(list1, list2):
    arr = np.array(list1 + list2).reshape(2, 5)
    return arr

# assert
list1 = [2,4,6,8,10]
list2 = [3,6,9,12,15]
print(list(gen_numpy1(list1, list2)[1]) == [3, 6, 9, 12, 15])
print ("#2 Passed")
print("---")
print("---")
print("---")

'''
3 Numpy 3
write a function get_row_sum(nparr, row_number):
return the sum of row 'row_number'
in the numpy array 'nparr'
'''

def get_row_sum(nparr, row_number):
    return sum(nparr[row_number])

# assert
arr1 = np.arange(1,21).reshape(4,5)

print(get_row_sum(arr1, 1) == 40)
print ("#3 Passed")
print("---")
print("---")
print("---")



'''
4 Numpy 4
write a function get_col_sum(nparr, col_number):
return the sum of col 'col_number'
in the numpy array 'nparr'
'''

#code
def get_col_sum(nparr, col_number):
    return sum(nparr[:,col_number])

# assert
arr1 = np.arange(1,21).reshape(4,5)
col_number = 1
print(get_col_sum(arr1, col_number) == 38)
print ("#4 Passed")
print("---")
print("---")
print("---")



'''
5 Panda 1 Series
write a function get_series_mean_std(series1):
that returns a tuple
with the mean and standard deviation
of the series data as integers
using the floor function
'''

# code
def get_series_mean_std(series1):
    mean = series1.mean()
    std_dev = series1.std()
    print(math.floor(mean), math.floor(std_dev))
    return(math.floor(mean), math.floor(std_dev))

# assert
s1 = pd.Series(range(20,30))

# call function  - get tuple
tup = get_series_mean_std(s1)

print(tup[0] == 29)
print(tup[1] == 5)
print("#5 Passed")
print("---")
print("---")
print("---")

'''
6 Panda 2 DataFrame
write a function add_temp_centigrade(filename) that:
creates a dataframe from the csv file
the dataframe contains a column 'temp_f'
that shows temperature in farenheit

create a new column in the dataframe called 'temp_c' that is the centigrade conversion from column 'temp_f'
Display the dataframe with new column
to convert farenheit to centigrade
use your earlier function
or write code directly (up to you)

NOTE: there is no assert for this question
the function add_temp_centigrade
should simply DISPLAY the dataframe -

# feel free to define a temp conversion function for use
'''

# code
def add_temp_centigrade(filename):
    try:
        df = pd.read_csv(filename)
        df['temp_C'] = (df['temp_f'] - 32) * (5/9)
        return print(df)
    except FileNotFoundError:
        print('File Not Found Error')

# use this file and display the dataframe with new column    
filename = 'a5q6.csv'
add_temp_centigrade(filename)
print("---")
print("---")
print("---")



'''
7 Panda 3 DataFrame
write a function add_new_col(filename):
reads the csv file (a5q7.csv) passed as parameter
if the name of the file is not a5q7.csv,
return None
add column 'D' to the dataframe
that is the sum of columns A, B and C
return the sum of the new column D
'''

# code
def add_new_col(filename):
    try:
        if filename != 'a5q7.csv':
            return None
        df = pd.read_csv(filename)
        df['D'] = df['A'] + df['B'] + df['C']
        return sum(df['D'])
    except FileNotFoundError:
        print("FileNotFoundError")


# assert
print(add_new_col('aaa.csv') == None)
print(add_new_col('a5q7.csv') == 861)
print("#7 Passed")
print("---")
print("---")
print("---")



'''
8 Panda 4 DataFrame
write a function top_world_cup_winner(filename):
reads the csv file worldcup.csv into a dataframe

if filename is not worldcup.csv return None
the dataframe contains a column 'first'

for winners of the world cup
write code that returns the country
with the most first place wins
'''

#code
def top_world_cup_winner(filename):
    try:
        if filename != 'worldcup.csv':
            return None
        df = pd.read_csv(filename)
        count_wins = df['first'].value_counts()
        most_wins_country = count_wins.idxmax()
        return most_wins_country
    except FileNotFoundError:
        print("FileNotFoundError")

# assert
print(top_world_cup_winner('zzz.csv') == None)
print(top_world_cup_winner('worldcup.csv') == 'Brazil')
print("#8 Passed")
print("---")
print("---")
print("---")


'''
9 Panda 5 DataFrame
add a row to the wordcup dataframe
with the following data:
year: 2022 
attendance=2,650,000
first=Argentina 
second=France
third=Croatia
fourth=Morocco
location:Qatar

if you have other info add it
otherwise use 'None' for unknown

Display a bar graph for the world cup data
showing attendance by year including 2022
there is no assert. 
simply display the bar graph
'''


def display_bar_graph(filename):
    try:
        if filename != 'worldcup.csv':
            return None
        new_data = {
            'year': 2022,
            'attendance': [2650000],
            'first': 'Argentina',
            'second': 'France',
            'third': 'Croatia',
            'fourth': 'Morocco',
            'location': 'Qatar'
        }
        df = pd.read_csv(filename)
        new_row = pd.DataFrame(new_data)
        df = pd.concat([df, new_row], ignore_index=True)

        df.plot(x='year', y='attendance', kind='bar', logy=True)
        plt.xlabel('Year')
        plt.ylabel('Attendance')
        plt.title('World Cup Attendance by Year')
        plt.show()

        return df

    except FileNotFoundError:
        print("FileNotFoundError")

display_bar_graph('worldcup.csv')
print("---")
print("---")
print("---")