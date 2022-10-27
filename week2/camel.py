#implementation of the camelCase exercise
import re

#word convert camel to snake
def convert(camel):
      word = re.split('(?=[A-Z])', camel)
      snake = word[0]
      i = 1 
      while i < len(word):
            snake = snake + '_' + word[i].lower()
            i += 1
      return snake

#main function  
def main():
        camel = input("camelCase: ")
        snake = convert(camel)
        print(f"snake_case: {snake}")
    
if __name__ == "__main__":
    main()