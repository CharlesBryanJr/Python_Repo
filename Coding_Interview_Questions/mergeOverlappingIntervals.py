'''merge_overlapping_intervals.py'''
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
    # a non empty two dimensional array of aribitary intervals

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
# interval == two integers
# interval[0] = start of interval
# interval[1] = end of interval

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement


Output(array): overlapping_intervals
# new intervals in any order
'''

'''
# Time: O(nlog(n)) | # Space: O(n)
Main Function
Input(array): intervals

    # sort the array so that the start of each interval is in ascending order
        # we can sort this 2D array by using the lambda function


    # we need an array data structure to store our output overlapping_intervals array

    # next, we need to create a varaible that will store the current interval
        # the current interval will be the last interval that was appended to our output array
        # the current interval's start will remain constant
        # the current interval's end can and will be updated if needed

    # append the current interval to the array
        # after the input has been sorted
            # the first interval's start will be the smallest value
            # and the smallest value should be also the first interval's start in the output array

    # iterate through the sorted intervals
        # if the current_interval_end >= interval_start:
            # then, we have found an overlapping interval
            # We need to update the current_interval_end in the output array
                # if current_interval_end > interval_end
                    # then the interval is encompassed within the current interval in the output array
                    # so no update if needed
                # if the interval_end > current_interval_end
                    # then we need to expand the current_interval_end
                    # so, update current_interval_end == interval_end
        # if the current_interval_end < interval_start:
            # then its time to append the interval
            # update current_interval == interval
                # because we are done with the old current_interval
                # and the next iteration needs the an updated current_interval
            # append the current_interval to the output array
                # the current_interval's start is now the smallest value remaining
                # if need the current_interval's end will be updated

Output(array): overlapping_intervals
# new intervals in any order
'''


# Time: O(nlog(n)) | # Space: O(n)
def merge_overlapping_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    overlapping_intervals = []

    current_interval_start = intervals[0][0]
    current_interval_end = intervals[0][1]

    for idx in range(len(intervals)):
        interval_start = intervals[idx][0]
        interval_end = intervals[idx][1]

        if current_interval_end >= interval_start:
            if current_interval_end < interval_end:
                current_interval_end = interval_end
        else:
            current_interval = [current_interval_start, current_interval_end]
            overlapping_intervals.append(current_interval)
            current_interval_start = interval_start
            current_interval_end = interval_end

    if len(overlapping_intervals) == 0:
        current_interval = [current_interval_start, current_interval_end]
        overlapping_intervals.append(current_interval)

    if intervals[-1][1] != overlapping_intervals[-1][1]:
        last_interval = [current_interval_start, current_interval_end]
        if last_interval != overlapping_intervals[-1]:
            overlapping_intervals.append(last_interval)

    return overlapping_intervals


# Time: O(nlog(n)) | # Space: O(n)
def mergeOverlappingIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    overlapping_intervals = []

    current_interval = intervals[0]
    overlapping_intervals.append(current_interval)

    for idx in range(len(intervals)):
        interval = intervals[idx]
        current_interval_start = current_interval[0]
        current_interval_end = current_interval[1]

        interval_start = interval[0]
        interval_end = interval[1]

        if current_interval_end >= interval_start:
            if current_interval_end < interval_end:
                current_interval[1] = interval_end
        else:
            overlapping_intervals.append(interval)
            current_interval = interval

    return overlapping_intervals


intervals = [[1, 2],
             [3, 5],
             [4, 7],
             [6, 8],
             [9, 10]]
print("intervals:", intervals)
print("merge_overlapping_intervals", merge_overlapping_intervals(intervals))
print("mergeOverlappingIntervals:", mergeOverlappingIntervals(intervals))
print(" ")

intervals = [[0, 0],
             [0, 0],
             [0, 0],
             [0, 0],
             [0, 0],
             [0, 0],
             [0, 1]]
print("intervals:", intervals)
print("merge_overlapping_intervals", merge_overlapping_intervals(intervals))
print("mergeOverlappingIntervals:", mergeOverlappingIntervals(intervals))
print(" ")

intervals = [
    [89, 90],
    [-10, 20],
    [-50, 0],
    [70, 90],
    [90, 91],
    [90, 95]
]
print("intervals:", intervals)
print("merge_overlapping_intervals", merge_overlapping_intervals(intervals))
print("mergeOverlappingIntervals:", mergeOverlappingIntervals(intervals))
print(" ")

intervals = [
    [1, 22],
    [-20, 30]
]
print("intervals:", intervals)
print("merge_overlapping_intervals", merge_overlapping_intervals(intervals))
print("mergeOverlappingIntervals:", mergeOverlappingIntervals(intervals))
print(" ")
