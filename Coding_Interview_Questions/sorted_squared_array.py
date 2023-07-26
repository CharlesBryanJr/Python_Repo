'''sorted_squared_array.py'''
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


- Sorting

Input:
- Intuitive
    - array of ints
        - sorted in ascending order
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Arrays
			- Empty array
			- Nested or not nested

Observations / Clarifying Questions / Insights:
- larger sqaure values are on the edges of the given array
    - and the need to end on the right side of the output array
-

Output:
- sorted array of squares of the the orginal array
'''

# O(nlog(n)) time | O(n) space
def sorted_squared_array(array):
    postive_array = []
    for idx in range(len(array)):
        num = array[idx]
        postive_array.append(num * num)

    postive_array.sort()
    return postive_array


# O(n) time | O(n) space
def sortedSquaredArray(array):
    square_array = []
    for idx in range(len(array)):
        square_array.append(0)

    left_idx = 0
    right_idx = len(array) - 1

    for idx in reversed(range(len(square_array))):
        left_value = abs(array[left_idx])
        right_value = abs(array[right_idx])

        if left_value > right_value:
            square_array[idx] = left_value * left_value
            left_idx += 1
        else:
            square_array[idx] = right_value * right_value
            right_idx -= 1

    return square_array


array = [1, 2, 3, 5, 6, 8, 9]
print("array:", array)
print("sorted_squared_array:", sorted_squared_array(array))
print("sortedSquaredArray:", sortedSquaredArray(array))
print(" ")

array = [-5, -4, -3, -2, -1]
print("array:", array)
print("sorted_squared_array:", sorted_squared_array(array))
print("sortedSquaredArray:", sortedSquaredArray(array))
print(" ")

array = [-1, -1, 2, 3, 3, 3, 4]
print("array:", array)
print("sorted_squared_array:", sorted_squared_array(array))
print("sortedSquaredArray:", sortedSquaredArray(array))
print(" ")
