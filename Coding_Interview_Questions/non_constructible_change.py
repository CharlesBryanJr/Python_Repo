'''non_constructible_change.py'''
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
# array of values
# find the minimum sum of values that cannot be created
# coins can not reused to make new value

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

Observations / Clarifying Questions / Insights:
- same coin value can appear more than once
- postive integers

- simplest / smallest problem
	- find n > sum + 1
    - where n is a value in an array

Output: the minimum sum of money that you can NOT create
-
'''

# find n > sum + 1
# where n is a value in an array

# O(nlog(n)) time | O(1) space
def nonConstructibleChange(coins):
    if len(coins) == 0:
        return 1
    coins.sort()
    change_created = 0

    for coin in coins:
        if coin > change_created + 1:
            return change_created + 1

        change_created += coin

    return change_created + 1


coins = [5, 7, 1, 1, 2, 3, 22]
print("coins:", coins)
print("nonConstructibleChange:", nonConstructibleChange(coins))
print(" ")

coins = [1, 1, 1, 1, 1]
print("coins:", coins)
print("nonConstructibleChange:", nonConstructibleChange(coins))
print(" ")

coins = [5, 6, 1, 1, 2, 3, 43]
print("coins:", coins)
print("nonConstructibleChange:", nonConstructibleChange(coins))
print(" ")

# _recursion
# _iteration
print(" ")