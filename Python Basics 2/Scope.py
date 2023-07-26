x = 1

def foo():
    x=0
    print(x)

foo()
print(x)
print(" ")


def add_5(y):
    y = y + 5
    print(y)

y = 10
print(y)
add_5(y)
print(y)

print(" ")

def append_5(z):
    #z = z[:]
    z.append(5)
    print(z)

z = []
print(z)
append_5(z)
print(z)