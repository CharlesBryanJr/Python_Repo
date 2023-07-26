'''args_kwargs.py'''
# pylint: disable=E1101
print(" ")

def sum_items(*args, **kwargs):
    '''sum_items'''
    print(sum(args))
    print(args)
    print(kwargs)
    print(" ")


sum_items(1, 2, 3, k=2, a=13)
sum_items(1, k=938234)
sum_items()

print(" ")

def sum_items_1(a, b, c):
    '''sum_items_1'''
    print(a, b, c)
    return a + b + c

args1 = [4, 5, 0]
args2 = "572"

x = sum_items_1(*args1)
print(x)

y = sum_items_1(*args2)
print(y)

print(" ")

kwargs1 = {"a": 5, "c": 10, "b": 5}
xx = sum_items_1(**kwargs1)
print(xx)

print(" ")

values = [1,3,4,5,6,78,98,5,3,5]
print(*values)

print(" ")
print(" ")
print(" ")


def test(p1, *args, **kwargs):
    print(p1, args, kwargs)

test(1, 5, 5, 5, k=3, ahah = "777")
print(" ")
args = [5, 5, 5]
kwargs = {"k": 3, "ahah": "777"}
test(1, *args, **kwargs)

print(" ")
print(" ")


def get_args_and_kwargs(*args, **kwargs):
    number_of_args = len(args) + len(kwargs)
    num = kwargs.get("num", 0)

    if not isinstance(num, int) and not isinstance(num, float):
        return False

    return number_of_args >= 4 and num > 5

