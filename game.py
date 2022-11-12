#implement game.py
from random import randint

def main():
    while(True):
        level = int(input("Level: "))
        if level > 0:
            random_num = randint(1,level)
            while(True):
                guess = int(input("Guess: "))
                if guess == random_num:
                    print("Just right!")
                    exit()
                elif guess < random_num and guess > 0:
                    print("Too small!")
                elif guess > random_num:
                    print("Too large!")
                else:
                    pass
        else: 
            pass
main()