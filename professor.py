#implement professor.py
import random

def main():
    level = int(get_level())
    score = generate_integer(level)
    print(f"Score: {score}")

def get_level():
    while(True):
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            return level

def generate_integer(level):
    counter = 10 
    correct = 0
    level = int(level)
    if level == 1:
        while counter != 0:
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
            user = input(f"{num1} + {num2} = ")
            if check(user, num1, num2) == True:
                correct += 1
            counter -= 1
        return correct
            
    elif level == 2:
        while counter != 0:
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
            user = input(f"{num1} + {num2} = ")
            if check(user, num1, num2) == True:
                correct += 1
            counter -= 1
        return correct
    else:
        while counter != 0:
            num1 = random.randint(100,999)
            num2 = random.randint(100,999)
            user = input(f"{num1} + {num2} = ")
            if check(user, num1, num2) == True:
                correct += 1
            counter -= 1
        return correct

def check(user, num1, num2):
    counter = 3
    answer = num1 + num2
    while counter != 0:
        counter -= 1
        if user == str(answer):
            return True
        else:
            print("EEE")
            if counter == 0:
                print(f"{num1} + {num2} = {answer}")
                return False
            user = input(f"{num1} + {num2} = ")

    


if __name__ == "__main__":
    main()