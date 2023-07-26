print(" ")

user_name = input("Input your user name: ")
password = input("Input your password : ")
print(" ")

MIN_PASSWORD_LENGTH = 6

if (len(password) > MIN_PASSWORD_LENGTH):
    print(f"{password} is valid.")
else:
    print(f"{password} is not valid.")
    print(
        f"You need to add {MIN_PASSWORD_LENGTH-len(password)} more characters")

print(" ")
