'''zero_sum_subarray.py'''
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

Input(array): nums
# Intuitive
    # an array of numbers

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
		# Dictionaries (Hashmaps)
			# Collisions

Observations / Clarifying Questions / Insights:
# zero sum subarray == all values add to zero
# subarray == any contiguous section of the array

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement

Output(boolean):
    # True, if a zero sum subarray exist
    # False, if a zero sum subarray does not exist
'''

'''
# Time: O() | # Space: O()
Main Function
Input(array): nums

Output(boolean):
    # True, if a zero sum subarray exist
    # False, if a zero sum subarray does not exist
'''


# Time: O(n) | # Space: O(n)
def zeroSumSubarray(nums):
    running_sum_dict = {0: True}

    running_sum = 0
    for num in nums:
        running_sum += num
        if running_sum in running_sum_dict:
            return True
        running_sum_dict[running_sum] = True

    return False


nums = [1, 2, -2, 3]
print("nums:", nums)
print("zeroSumSubarray:", zeroSumSubarray(nums))
print(" ")

nums = [-1, 2, 3, 4, -5, -3, 1, 2]
print("nums:", nums)
print("zeroSumSubarray:", zeroSumSubarray(nums))
print(" ")

nums = [1, 2, 3, 4, 0, 5, 6, 7]
print("nums:", nums)
print("zeroSumSubarray:", zeroSumSubarray(nums))
print(" ")

# _recursion
# _iteration
print(" ")
