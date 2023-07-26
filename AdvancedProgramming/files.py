'''files.py'''
# pylint: disable=E1101
print(" ")

#file = open("file.txt", "r")
#print(file.read())
#file.close()

with open("file.txt", "r") as file:
    print(file.read())
    print(" ")
    print(file.readlines())
    print(" ")
    line1 = file.readlines()
    print([line1.strip()])

print(" ")