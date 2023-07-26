'''caesar_cipher'''
print(" ")


def caesar_cipher(string, offset):
    '''caesar_cipher'''
    while not str(offset).isdigit() and int(offset) > 26:
        print('Please enter a valid number no greater than 26')
        offset = input("Input offset: ")

    incorrect_string = True

    while incorrect_string:
        for char in string:
            if char.isdigit is True:
                print("Error: String contains an int.")
                break

        else:
            incorrect_string = False

    new_string = ""

    for char in string:
        new_char = ord(char) - offset

        if new_char < 98:
            wrap = 98 - new_char
            new_char = 124 - wrap

        new_string += chr(new_char)

    print(string)
    print(new_string)


caesar_cipher("hello", 3)
print(" ")
caesar_cipher("apple", 5)
print(" ")


def caesar_cipher2(string, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    encoded_string = ''

    for character in string:
        position = alphabet.index(character)
        offset_position = position - offset
        # No need to handle negative positions because of negative indexing
        encoded_character = alphabet[offset_position]
        encoded_string += encoded_character

    return encoded_string
