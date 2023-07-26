print(' ')
is_old = True
is_licenced = True

if is_old and is_licenced:
    print("*** starting engine ***")
else:
    print("not old enough")

print(' ')
result = 'Ok' if is_old and is_licenced else 'Not Okay'
print(result)
print(' ')
print('Ok') if is_old and is_licenced else print('Not Okay')

# Indentation In Python
print(' ')
strings = [
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
    input("Enter a string: "),
]

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

final_string = strings[num1] + strings[num2] + strings[num3]
print(final_string)

