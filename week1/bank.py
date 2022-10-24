#implement bank greeting implementation

def main():
    greeting = input("Greeting: ")
    greet = greeting.split()[0]
    if greet == "hello":
        print("$0")
    elif greet == "Hello":
        print("$0")
    elif greet == "Hello,":
        print("$0")
    elif greet[0] == "h" or "H":
        print("$20")
    else:
        print("$100")

main()