'''abstract_classes.py'''
import random
print(" ")

class AbstractGame:
    '''AbstractGame'''

    def start(self):
        '''start'''

        while True:
            start = input("Would you like to play? : ")
            if start.lower() == 'yes':
                break
        
        self.play()
    
    def end(self):
        '''end'''
        print("The game has ended.")
        self.reset()
    
    def play(self):
        '''play'''
        raise NotImplementedError("Implementation for a play() not defined")
    
    def reset(self):
        '''reset'''
        raise NotImplementedError("Implementation for a reset() not defined")


class RandomGuesser(AbstractGame):
    '''RandomGuesser'''

    def __init__(self, rounds) -> None:
        super().__init__()
        self.rounds = rounds
        self.round = 0
    
    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}.")
            print("Begin!")

            random_number = random.randint(0,10)
            while True:
                print(" ")
                guess = input("Input a number between 1-10: ")
                if int(guess) == random_number:
                    print("Winner!")
                    break
        
        self.end()

class Game2(AbstractGame):
    
    def play(self):
        pass
    
    def reset(self):
        pass


games = [RandomGuesser(1), Game2()]

for game in games:
    game.start()
    print(" ")

print(" ")