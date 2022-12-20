#implement um exercise
import re

def main():
    print(count(input("TEXT: ")))

def count(text):
    count = 0
    text = text.split()
    for word in text:
        print(word)
        if re.search("^um", word):
            count += 1
    return count

if __name__ == "__main__":
    main()
