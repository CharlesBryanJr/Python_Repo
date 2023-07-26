print(" ")
x = [1,2,2,2,3,4,5,3,4]
set_x = set(x)

print(x)
print(" ")
print(set_x)

print(" ")

numbers = set()

while True:
    num = int(input("Number: "))

    if num in numbers:
        break

    numbers.add(num)