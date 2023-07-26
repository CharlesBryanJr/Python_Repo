print(' ')
characters = {}

string = "Hello World"

for char in string:
    characters[char] = characters.get(char, 0) + 1

print(characters)

print(' ')


counts = {}

while True:
    num = input("Number (enter q to quit): ")

    if num == "q":
        break

    num = int(num)
    counts[num] = counts.get(num, 0)+1

print(' ')
print(counts)

print(' ')
