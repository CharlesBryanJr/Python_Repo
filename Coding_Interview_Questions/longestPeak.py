'''longestPeak.py'''
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

# Searching
# Sorting


Input():
# Intuitive
    -  an array of integers
# Primitive Types
		# Numbers
			# Zero (0)
			# NULL or nil
			# Negative Numbers
			# Floats or Doubles (clarifies if Ints only?)
			# Min/Max Int

Observations / Clarifying Questions / Insights:
- peak ==
    - adjacent integers that strictly increase until the tip
    - then
    - adjacent integers that strictly decreasing
- tip == highest value in the peak
- 3 integer minimum

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	# reverse this statement

Output(int): longest_peak_length
- the length of the longest peak in the array

'''

'''
Algo Time: O() | # Space: O():
Main Function
Input():
find all peaks
compare all peaks
return the length of the largest one

Output(int): longest_peak_length
- the length of the longest peak in the array

'''

# Time: O(n) | # Space: O(1)
def longestPeak(array):
    longest_peak_length = 0
    peak_locations = []
    for idx in range(1, len(array) - 1):
        last_num = array[idx - 1]
        num = array[idx]
        next_num = array[idx + 1]

        if num > last_num and num > next_num:
            peak_locations.append(idx)

    for peak in peak_locations:
        peak_length = 1
        peak_length += count_left(array, peak)
        peak_length += count_right(array, peak)

        if peak_length > longest_peak_length:
            longest_peak_length = peak_length

    return longest_peak_length


def count_left(array, peak):
    peak_length = 0
    for idx in reversed(range(peak + 1)):
        last_num = array[idx]
        num = array[idx - 1]
        if num >= last_num:
            return peak_length
        peak_length += 1
        last_num = num
    return peak_length


def count_right(array, peak):
    peak_length = 0
    last_num = array[peak]
    for idx in range(peak + 1, len(array)):
        num = array[idx]
        if num >= last_num:
            return peak_length
        peak_length += 1
        last_num = num
    return peak_length


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print("array:", array)
print("longestPeak:", longestPeak(array))
print(" ")

array = [1, 2, 3, 3, 2, 1]
print("array:", array)
print("longestPeak:", longestPeak(array))
print(" ")

array = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
print("array:", array)
print("longestPeak:", longestPeak(array))
print(" ")
