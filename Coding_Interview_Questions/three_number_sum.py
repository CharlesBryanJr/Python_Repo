'''three_number_sum.py'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
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

given:
- a non empty array of distinct integers
- an integer target sum

return:
- a two dimensional array of
- all triplets that sum to the given integer target sum

note:
- ascending order for numbers in each triplet
- ascending order for triplets themselves, with respect to the numbers they hold

targetSum = a + b + c
a = targetSum - b - c
b = targetSum - a - c
c = targetSum - a - b
'''

# Time: O(n^2) | # Space: O(n)
def threeNumberSum(array, targetSum):
    three_number_sum = []
    array.sort()

    for idx in range(len(array) - 2):
        num = array[idx]
        left_idx = idx + 1
        right_idx = len(array) - 1

        while left_idx < right_idx:
            left_num = array[left_idx]
            right_num = array[right_idx]
            current_sum = num + left_num + right_num
            if current_sum == targetSum:
                three_number_sum.append([num, left_num, right_num])
                left_idx += 1
                right_idx -= 1
            elif current_sum < targetSum:
                left_idx += 1
            elif current_sum > targetSum:
                right_idx -= 1

    return three_number_sum


array1 = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum1 = 0
print("array1:", array1)
print("targetSum1:", targetSum1)
print(threeNumberSum(array1, targetSum1))
print(" ")

array2 = [1, 2, 3]
targetSum2 = 6
print("array2:", array2)
print("targetSum2:", targetSum2)
print(threeNumberSum(array2, targetSum2))
print(" ")

array3 = [8, 10, -2, 49, 14]
targetSum3 = 57
print("array3:", array3)
print("targetSum3:", targetSum3)
print(threeNumberSum(array3, targetSum3))
print(" ")


# _recursion
# _iteration
print(" ")
