print(" ")
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(b)
print(c)
print(other)
print(d)

matrix = [
    [1, 2, 3, 2, 3],
    [True, False],
    ["Charles"],
    [77, "hi", 4.5]
]

print(" ")
print(list(range(1, 100)))
print(" ")

STRING_JOIN = ' '.join(["Hi", "my", "name", "is", str(matrix[2])])
print(STRING_JOIN)
print(" ")

print(matrix)
print(" ")

new_matrix = matrix.copy()
new_matrix.reverse()
print(new_matrix)
print(" ")

print(matrix[1].index(False))
print(" ")

print("hi" in matrix[3])
print(" ")

print(matrix[0].count(2))
print(" ")

print(sorted(matrix[0]))
print(" ")
matrix[0].sort()
print(matrix[0])
print(" ")

# List Methods
# Adding
matrix[0].append(str(100))
matrix.insert([0][0], -1)
matrix[2].extend(["python > JavaScript"])
print(matrix)
print(" ")

# Removing
matrix[1].pop(1)
matrix[1].pop()
matrix[2].remove(True)
matrix[4].clear()
print(matrix)
print(" ")
