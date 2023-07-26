'''lambda_functions.py'''
# pylint: disable=E1101
print(" ")

func = lambda x, y, z=0: print(x + y + z)
func(1,2,5)
print(func(1,2,5))
print("----")
print("----")
print("----")

def sort_func(x):
    return x[1]

lst1 = [(1, 2), (-2, -4), (3, 4), (0, 0)]
lst1.sort(key=sort_func)
print(lst1)
print(" ")

lst2 = [(1, 2), (-2, -4), (3, 4), (0, 0)]
lst2.sort(key= lambda x: x[1] )
print(lst2)
print(" ")
print("----")
print("----")
print("----")

def mul1(x):
    def mul2(y):
        return x * y

    return mul2

result2 = mul1(2)
print(result2)
print(result2(3))
print(mul1(2)(3))
print(" ")

mul = lambda x: lambda y: x * y
result1 = mul(2)
print(result1)
print(result1(3))
print(mul(2)(3))
print(" ")


print(" ")

add_values = lambda x, y, z : x + y + z
#add_values = lambda x, y, z : sum([x, y, z])

max_length = lambda x, y: max(len(x), len(y))

create_set = lambda x, y: set(x).union(y)
#create_set = lambda x, y: set(x) | set(y)
#create_set = lambda x, y: set(x + y)

print(" ")
