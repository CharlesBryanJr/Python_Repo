'''firstDuplicateValue.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=C0200
print(" ")

'''
Question:
-

Type of Question:
- Array
	- draw indices
	- sorting
    - multiple pointers
    - mutating the current index or later index to count
    - hashing the index values
		- running sums
		- sliding windows
			- start_of_window
			- end_of_window

# Recursion
	# the solution depends on solutions to smaller instances of the same problem
		# define the smaller instance of the problem
			# translate the for/while loop into a base case
	# will iterate/traverse until the function can return a value (base case)
		# always include return statment
	# base case == the smallest instance of the problem that can be solved directly
	# to keep track of element, store the element in a variable that connected to the recursion call
	# running variables left to right
			# arguments
	# running variables right to left
			# return statment
	# Recursive functions often take a sub array of the original array
	# the outcome of a recursive function will affect code on lines after it
	# To optimize use memoization
		# store the answer to recursive calls in a hash table
	# 1. Base Case
	# 2. Action
	# 3. update variables
	# 4. Recursion
		if idx >= len(array):

# Searching
# Sorting


Input():
# Intuitive
- array of integers between 1 and n, inclusive
- n == length of the array

# Primitive Types
		# Numbers
			# Zero (0)
			# NULL or nil
			# Negative Numbers
			# Floats or Doubles (clarifies if Ints only?)
			# Min/Max Int
		# Arrays
			# Empty array
			# Nested or not nested


Observations / Clarifying Questions / Insights:
# from left to right
# mutate the input array if needed
# since the nums in the array are limited from 1 to n
	each idx can represent a num

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement

Output(int): num
- return -1, if no duplicates exist
- return num, if duplicates exist
'''

'''
# Time: O() | # Space: O()
Main Function
Input(array): array

Output(int): num
- return -1, if no duplicates exist
- return num, if duplicates exist
'''


# Time: O(n) | # Space: O(n)
def firstDuplicateValue_n(array):
    dictionary = {}
    for num in array:
        if num in dictionary:
            return num
        dictionary[num] = True
    return -1

# Time: O(n) | # Space: O(1)
def firstDuplicateValue(array):
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1
    return -1


array = [2, 1, 5, 2, 3, 3, 4]
print("array:", array)
print("firstDuplicateValue_n:", firstDuplicateValue_n(array))
print("firstDuplicateValue_recursion:", firstDuplicateValue_recursion(array))
print("firstDuplicateValue:", firstDuplicateValue(array))
print(" ")
'''
array = [2, 2, 2, 2, 2, 2, 2, 2, 2]
print("array:", array)
print("firstDuplicateValue_nn_1:", firstDuplicateValue_nn_1(array))
print("firstDuplicateValue_n_n:", firstDuplicateValue_n_n(array))
print("firstDuplicateValue_n_1:", firstDuplicateValue_n_1(array))
print("firstDuplicateValue_n_1:", firstDuplicateValue_n_1(array))
print(" ")

array = [9, 13, 6, 2, 3, 5, 5, 5, 3, 2, 2, 2, 2, 4, 3]
print("array:", array)
print("firstDuplicateValue_nn_1:", firstDuplicateValue_nn_1(array))
print("firstDuplicateValue_n_n:", firstDuplicateValue_n_n(array))
print("firstDuplicateValue_n_1:", firstDuplicateValue_n_1(array))
print(" ")

# _recursion
# _iteration
print(" ")
'''
