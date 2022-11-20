#implementation of fuel exercise
def main():
    while True:
        try:
            fraction =  input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    fraction = fraction.split("/")
    num = fraction[0]
    den = fraction[1]
    if num.isnumeric() == True and den.isnumeric() == True:
        den = int(den)
        num = int(num)
        if den != 0 and num <= den:
            percent = int((num/den) * 100)
            return percent
        elif num > den:
            raise ValueError
        else:
            raise ZeroDivisionError
    else:
        raise ValueError
    
def gauge(percent):
    percent = int(percent)
    if percent >= 99:
        return "F"
    elif percent == 0:
        return "E"
    else:
        return f"{percent}%"



if __name__ == "__main__":
    main()