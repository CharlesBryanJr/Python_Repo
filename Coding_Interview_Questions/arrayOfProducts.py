'''arrayOfProducts.py'''
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
# Stacks
# Strings
# Tries

Input(array): array
# Intuitive
    # a non empty array of integers
# Primitive Types
	# Numbers
		# Zero (0)
		# NULL or nil
		# Negative Numbers
		# Floats or Doubles (clarifies if Ints only?)
		# Min/Max Int

Observations / Clarifying Questions / Insights:
# can not use division
# the value at any index in the array
#   == left_products * right_products

Cases:
#

# simplest / smallest problem
	#

# If I knew / had this....
	#
	# reverse this statement

Output(array): array_of_products
- an array of the same length of the given array
- each element is equal the product of every other number in the given array
'''

'''
# Time: O() | # Space: O()
Main Function
Input(array): array

Output(array): array_of_products
- an array of the same length of the given array
- each element is equal the product of every other number in the given array
'''

# Time: O(n^2) | # Space: O(n)
def array_of_products_n_n(array):
    array_of_products = []
    for i in range(len(array)):
        product = 1
        for ii in range(len(array)):
            if i == ii:
                continue
            num = array[ii]
            product *= num

        array_of_products.append(product)

    return array_of_products

# Time: O(n) | # Space: O(n)
def arrayOfProducts_n(array):
    array_of_products = []

    product = 1
    zero_count = 0
    for idx in range(len(array)):
        num = array[idx]
        if num == 0:
            zero_count += 1
            continue
        product *= num

    if zero_count == 1:
        for idx in range(len(array)):
            num = array[idx]
            if num == 0:
                array_of_products.append(product)
                continue
            array_of_products.append(0)
        return array_of_products

    if zero_count > 1:
        for idx in range(len(array)):
            array_of_products.append(0)
        return array_of_products

    for idx in range(len(array)):
        num = array[idx]
        array_of_products.append(product // num)

    return array_of_products


# Time: O(n) | # Space: O(n)
def arrayOfProducts_iteration(array):
    array_of_products = [1] * len(array)

    left_running_product = 1
    for idx in range(len(array)):
        array_of_products[idx] = left_running_product
        left_running_product *= array[idx]

    right_running_product = 1
    for idx in reversed(range(len(array))):
        array_of_products[idx] *= right_running_product
        right_running_product *= array[idx]

    return array_of_products

'''
# Time: O(n) | # Space: O(n)
Main Function
Input(array): array

create an output array 
    # to store the products for each index
    - array_of_products = [0] * len(array)

call the recursive function and store the result in the 0th index of the output array
- array_of_products[0] = products(array, index, array_of_products, value_to_exclude)

    pass the orginal array
    pass index 
        # intialized to == 1
        - index = 1
    pass the output array
    pass the first value in the orginal array
        # this value will not be not be used in product calculation
        - left_products = array[0]

return the output array 
    - array_of_products

Output(array): array_of_products
- an array of the same length of the given array
- each element is equal the product of every other number in the given array
'''

# Time: O(n) | # Space: O(n)
def arrayOfProducts_recursion(array):
    array_of_products = [None] * len(array)

    index = 1
    left_products = array[0]
    array_of_products[0] = products(array, index, array_of_products, left_products)

    return array_of_products


'''
Recursive Function
Input(array, int, array, int): array, index, array_of_products, value_to_exclude

define the base case
    # since we need to loop through each index in the array
    # the base case or stopping condtion for looping can be reaching an index that does not exist 
    # return 1, because 1 has no effect in multiplication
    - if idx >= len(array):
        - return 1

set the current index value in the output array
    # the value at any index in the array == left_products * right_products
    - array_of_products[idx] = left_products * right_products

Output(int): right_products
- array[index] * right_products
- ea
'''

def products(array, index, array_of_products, left_products):
    if index >= len(array):
        return 1

    array_of_products[index] = left_products

    next_idx = index + 1
    updated_left_products = left_products * array[index]

    right_products = products(array, next_idx, array_of_products, updated_left_products)

    array_of_products[index] *= right_products

    updated_right_products = array[index] * right_products

    return updated_right_products

array = [5, 1, 4, 2]
print("array:", array)
print("array_of_products_n_n:", array_of_products_n_n(array))
print("arrayOfProducts_n:", arrayOfProducts_n(array))
print("arrayOfProducts_iteration:", arrayOfProducts_iteration(array))
print("arrayOfProducts_recursion:", arrayOfProducts_recursion(array))
print(" ")

array = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("array:", array)
print("array_of_products_n_n:", array_of_products_n_n(array))
print("arrayOfProducts_n:", arrayOfProducts_n(array))
print("arrayOfProducts_iteration:", arrayOfProducts_iteration(array))
print("arrayOfProducts_recursion:", arrayOfProducts_recursion(array))
print(" ")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("array:", array)
print("array_of_products_n_n:", array_of_products_n_n(array))
print("arrayOfProducts_n:", arrayOfProducts_n(array))
print("arrayOfProducts_iteration:", arrayOfProducts_iteration(array))
print("arrayOfProducts_recursion:", arrayOfProducts_recursion(array))
print(" ")

# _recursion
# _iteration
print(" ")
