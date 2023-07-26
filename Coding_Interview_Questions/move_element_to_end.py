'''move_element_to_end.py'''
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
given:
- an array of integers
- an integer

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

- Searching
- Sorting

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int

Observations / Clarifying Questions / Insights:
- mutate the input array
- order of rest of the integers do not matter

return:
- move all instances of the given integer to the end of the array
- return the array

'''

# Time: O(n) | # Space: O(1)
def moveElementToEnd(array, toMove):
    element_count = 1
    for idx in reversed(range(len(array))):
        num = array[idx]
        if num != toMove:
            continue

        switch_idx = len(array) - element_count
        switch_num = array[switch_idx]

        array[switch_idx] = num
        array[idx] = switch_num

        element_count += 1
    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
print("array:", array)
toMove = 2
print("toMove:", toMove)
print("moveElementToEnd:", moveElementToEnd(array, toMove))
print(" ")

array = [3, 3, 3, 3, 3]
print("array:", array)
toMove = 3
print("toMove:", toMove)
print("moveElementToEnd:", moveElementToEnd(array, toMove))
print(" ")

array = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
print("array:", array)
toMove = 5
print("toMove:", toMove)
print("moveElementToEnd:", moveElementToEnd(array, toMove))
print(" ")

# _recursion
# _iteration
print(" ")
