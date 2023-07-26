'''two_number_sum.py'''
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

Input:
- Intuitive
    - non empty array of distinct ints
    - int, represent the target sum
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
- the same index can not be used twice

Output:
- array of two ints that sum up to the target sum
- empty array if no two ints sum up to the target sum
'''

# O(n^2) time | O(1) space
def two_number_sum_n_n(array, target_sum):
    two_number_sum_array = []

    for i in range(len(array)):
        num1 = array[i]
        for ii in range(len(array)):
            num2 = array[ii]
            if num1 + num2 != target_sum:
                continue
            if i == ii:
                continue
            two_number_sum_array.append(num1)
            two_number_sum_array.append(num2)
            return two_number_sum_array

    return []

# O(n) time | O(n) space
def twoNumberSum_n(array, targetSum):
    two_number_sum_array = []
    two_number_sum_dict = {}

    for idx in range(len(array)):
        num1 = array[idx]
        two_number_sum_dict[num1] = idx

    for idx in range(len(array)):
        num1 = array[idx]
        num2 = targetSum - num1
        if num2 not in two_number_sum_dict:
            continue
        num2_idx = two_number_sum_dict[num2]
        if num2_idx == idx:
            continue
        two_number_sum_array.append(num1)
        two_number_sum_array.append(num2)
        return two_number_sum_array

    return []

# O(nlog(n)) time | O(1) space
def twoNumberSum3_nlogn(array, targetSum):
    array.sort()
    two_number_sum_array = []

    idx1 = 0
    idx2 = len(array) - 1
    while idx1 < idx2:
        num1 = array[idx1]
        num2 = array[idx2]
        if num1 + num2 < targetSum:
            idx1 += 1
        elif num1 + num2 > targetSum:
            idx2 -= 1
        else:
            two_number_sum_array.append(num1)
            two_number_sum_array.append(num2)
            break

    return two_number_sum_array


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print("array:", array)
print("targetSum:", targetSum)
print("two_number_sum_n_n:", two_number_sum_n_n(array, targetSum))
print("twoNumberSum:", twoNumberSum_n(array, targetSum))
print("twoNumberSum:", twoNumberSum3_nlogn(array, targetSum))
print(" ")

array = [4, 6, 1, -3]
targetSum = 3
print("array:", array)
print("targetSum:", targetSum)
print("two_number_sum_n_n:", two_number_sum_n_n(array, targetSum))
print("twoNumberSum:", twoNumberSum_n(array, targetSum))
print("twoNumberSum:", twoNumberSum3_nlogn(array, targetSum))
print(" ")

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 15
print("array:", array)
print("targetSum:", targetSum)
print("two_number_sum_n_n:", two_number_sum_n_n(array, targetSum))
print("twoNumberSum:", twoNumberSum_n(array, targetSum))
print("twoNumberSum:", twoNumberSum3_nlogn(array, targetSum))
print(" ")

# _recursion
# _iteration
print(" ")
print(" ")
