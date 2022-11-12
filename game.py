#implement game.py
from random import randint

def main():
    while(True):
        level = input("Level: ")
        while level.isnumeric() == False or int(level) <= 0:
            level = input("Level: ")
        random_num = randint(1,int(level))
        while(True):
            guess = input("Guess: ")
            while guess.isnumeric() == False or int(guess) <= 0:
                guess = input("Guess: ")
            guess = int(guess)
            if guess == random_num:
                print("Just right!")
                exit()
            elif guess < random_num:
                print("Too small!")
            else:
                print("Too large!")
main()