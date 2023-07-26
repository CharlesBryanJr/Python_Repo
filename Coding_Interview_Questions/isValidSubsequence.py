'''isValidSubsequence.py'''
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

Input:
- Intuitive
    - two non empty array of ints
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int

Observations / Clarifying Questions / Insights:
- all ints in the subsequence need to
    - appear in the array
    - appear in the same order

Output:
- True, if subsequence is an array
- False, if subsequence is not an array
'''

# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    sequence_idx = 0
    for idx in range(len(array)):
        array_num = array[idx]
        sequence_num = sequence[sequence_idx]
        if array_num != sequence_num:
            continue
        sequence_idx += 1
        if sequence_idx == len(sequence):
            return True

    return False

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print("array:", array)
print("sequence:", sequence)
print("isValidSubsequence:", isValidSubsequence(array, sequence))
print(" ")

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, -1, 8, 10]
print("array:", array)
print("sequence:", sequence)
print("isValidSubsequence:", isValidSubsequence(array, sequence))
print(" ")

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 22, 6, -1, 8, 10]
print("array:", array)
print("sequence:", sequence)
print("isValidSubsequence:", isValidSubsequence(array, sequence))
print(" ")

# _recursion
# _iteration
print(" ")