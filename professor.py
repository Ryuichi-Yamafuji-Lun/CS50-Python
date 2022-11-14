#implement professor.py
import random

def main():
    level = int(get_level())
    generate_integer(level)

def get_level():
    while(True):
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            return level

def generate_integer(level):
    counter = 10 
    correct = 0
    print(level)

if __name__ == "__main__":
    main()