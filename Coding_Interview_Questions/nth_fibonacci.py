'''file_name'''
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0621
# pylint: disable=W0102
print(" ")

# F(n) = F(n-1) + F(n-2)
# F(1) = 0
# F(2) = 1
# given n, return the nth Fibonacci number

# Time: O(2^n) | # Space: O(n)


def getNthFib(n):
    print(F"F({n})")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = getNthFib(n-1) + getNthFib(n-2)
        print(F"F({n}) = {a}")
        print(" ")
        return a


# Time: O(n) | # Space: O(n)
def getNthFib1(n, memoize={1: 0, 2: 1}):
    print(F"F({n})")

    if n in memoize:
        return memoize[n]

    else:
        memoize[n] = getNthFib1(n-1, memoize) + getNthFib1(n-2, memoize)
        print(F"F({n}) = {memoize}")
        print(" ")

        return memoize[n]


# Time: O(n) | # Space: O(1)
def getNthFib2(n):
    print(F"F({n})")
    base_case = [0, 1]
    counter = 3

    while counter <= n:
        next_fib = base_case[0] + base_case[1]
        base_case[0] = base_case[1]
        base_case[1] = next_fib
        counter += 1
        print(F"F({n}) = {base_case}")
        print(" ")

    return base_case[1] if n > 1 else base_case[0]


n = 6
memoize = {1: 0, 2: 1}
print(" ")
print(" ")
print("Time: O(2^n) | # Space: O(n): ", getNthFib(n))
print(" ")
print(" ")
print("# Time: O(n) | # Space: O(n): ", getNthFib1(n, memoize))
print(" ")
print(" ")
print("# Time: O(n) | # Space: O(1): ", getNthFib2(n))
print(" ")
