# strings are character arrays
# [start:stop:stepover]

NEW_STRING = 'Hello World'
print(NEW_STRING[0])
print(NEW_STRING[0:2])
print(" ")

for i in NEW_STRING:
    print(i)

print(" ")
print(NEW_STRING[::1])

print(" ")
print(NEW_STRING[::-1])


print(" ")
print(NEW_STRING[::-1].lower())
