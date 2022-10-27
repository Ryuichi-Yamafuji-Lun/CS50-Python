#twttr (shorten words) exercise implementation
def vowel_remove(message):
    for vowels in 'aeiou':
        message = message.replace(vowels,'')
    return message

def main():
    message = input("Input: ")
    message = vowel_remove(message)
    print(f"Output: {message}")

if __name__ == "__main__":
    main()