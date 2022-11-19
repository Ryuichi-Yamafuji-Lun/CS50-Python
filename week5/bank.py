#bank.py test


def main():
    greeting = input("Greeting: ")
    print(f"${amount(greeting)}")

def amount(greeting):
    greet = greeting.split()[0].lower()
    if greet == "hello":
        return 0
    elif greet == "hello,":
        return 0
    elif greet[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()