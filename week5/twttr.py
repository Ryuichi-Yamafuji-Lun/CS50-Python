#twttr for test
def shorten(message):
    for vowels in 'aeiouAEIOU':
        message = message.replace(vowels,'')
    return message

def main():
    message = input("Input: ")
    message = shorten(message)
    print(f"Output: {message}")

if __name__ == "__main__":
    main()