#implement response.py
import validators

def main():
    print(valid(input("What's your email address? ")))

def valid(email):
    if validators.email(email) == True:
        return "Valid"
    else:
        return "Invalid"
if __name__ == "__main__":
    main()