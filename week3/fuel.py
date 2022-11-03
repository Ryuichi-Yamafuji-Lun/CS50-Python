#implementation of fuel exercise
def main():
    x = 1
    while x != 0:
        fraction =  input("Fraction: ")
        fraction = fraction.split("/")
        x = calc(fraction[0], fraction[1])

def calc(num, den):
    if num.isnumeric() == True and den.isnumeric() == True:
        den = int(den)
        num = int(num)
        if den != 0 and num <= den:
            percent = (num/den) * 100
            if percent >= 99:
                print("F")
            elif percent == 0:
                print("E")
            else:
                print(f"{percent}%")
            return 0
        else:
            return 1
    else:
        return 1




main()