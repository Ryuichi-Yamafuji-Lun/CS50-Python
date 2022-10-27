#implementing vanity plate exercise
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    position = 3
    #check if condition of length 3-6 is maintained and if first two are letters
    if 2 < len(s) <=6 and s[:2].isalpha() == True:
        #counter to see how many alphabets there are at the beginning and check if it is only alphabet
        while s[:position].isalpha() == True and position <= len(s):
            position += 1
        #readjust position
        position -= 1
        x = len(s) - 1
        #check to see if it is only numeric at the end and if the beginning number starts with 0 
        if s[position:].isnumeric() == True and s[position:x] != "0":
            return 1
        else:
            return 0
    return 0

main()