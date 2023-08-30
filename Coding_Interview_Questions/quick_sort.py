'''merge_sort'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0621
# pylint: disable=W0102
print(" ")

'''
- What: A precise specification of the problem that the algorithm solves.
given an array of integers return a sorted version of the the input array

- How: A precise description of the algorithm itself.

Merge Sort
1. Divide the input array into two subarrays of roughly equal size.
2. Recursively merge sort each of the subarrays.
3. Merge the newly-sorted subarrays into a single sorted array.

- Why: A proof that the algorithm solves the problem it is supposed to solve.

- How fast: An analysis of the running time of the algorithm.

note:
-
'''

# Time: O(nlog(n)) | # Space: O(nlog(n))
def quickSort(array):
    base_case = (len(array) == 1)
    if base_case:
        return 1

    i = 0
    in_range = i < len(array)
    while in_range:
        left = i + 1
        right = len(array) - 1
        while right >= left:
            left_num_greater_than_pivot = array[left] > array[i]
            left_num_less_than_pivot = array[left] < array[i]
            right_num_less_than_pivot = array[right] < array[i]
            right_num_greater_than_pivot = array[right] > array[i]

            if left_num_greater_than_pivot and right_num_less_than_pivot:
                array[left], array[right] = array[right], array[left]
            elif left_num_less_than_pivot and right_num_greater_than_pivot:
                left += 1
                right -= 1
            elif left_num_less_than_pivot:
                left += 1
            elif right_num_greater_than_pivot:
                right -= 1
        array[i], array[right] = array[right], array[i]
        i += 1
        in_range = i < len(array)

    return array


array = [8, 5, 2, 9, 5, 6, 3]
print("array:", array)
array = [8, 5, 2, 9, 5, 6, 3]
print("quickSort:", quickSort(array))
array = [8, 5, 2, 9, 5, 6, 3]
print("quickSort:", quickSort(array))
print(" ")
'''
array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print("array:", array)
print("mergeSort:", quickSort(array))
array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]
print("merge_sort:", quickSort(array))
print(" ")

array = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59]
print("array:", array)
print("mergeSort:", quickSort(array))
array = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59]
print("merge_sort:", quickSort(array))
print(" ")
'''
