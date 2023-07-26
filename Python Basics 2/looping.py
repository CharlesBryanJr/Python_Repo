print(" ")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_tuple = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
count = 0

for element in my_list:
    count += element

print(count)
print(" ")

count = 0
for element in range(0, len(my_list)+1):
    count += element

print(count)
print(" ")

count = 0
for i, element in enumerate(my_list):
    count += element

print(count)
print(" ")

for i, element in enumerate(list(range(100))):
    print(i, element)
    if element == 50:
        print(" ")
        print(f'index of 50 is: {i}')
        print(" ")


print(" ")


picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = "*"
empty = " "
for image in picture:
    for pixel in image:
        if pixel:
            print(fill, end='')
        else:
            print(" ", end='')
    print("")

print(" ")


fill = "$"
empty = " "
for image in picture:
    for pixel in image:
        if pixel:
            print(fill, end='')
        else:
            print(" ", end='')
    print("")

print(" ")

some_list = [
    'a',
    'b',
    'c',
    'b',
    'd',
    'm',
    'n'
]

lastElement = ''

for current_element in some_list:
    for element in some_list:
        if element == current_element:
            print(f"Found duplicate : {element}")
            break
else:
    print("duplicate not found")
    

print(" ")
