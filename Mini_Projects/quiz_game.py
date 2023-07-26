'''quiz_game.py'''
# pylint: disable=E1101
print(" ")
print("Welcome to my computer quiz!")

playing = input("Do you want to play? : ")

if playing.lower() != "yes":
    print("Goodbye")
    print(" ")
    quit()


answer = input("What does CPU stand for? ")
if answer == "cnetral processing unit":
    print('Correct')

print(" ")