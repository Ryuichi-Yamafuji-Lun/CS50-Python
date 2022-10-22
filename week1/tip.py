#implementation of a tip calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#it is assumed that the user will input in the "$##.##"" format
def dollars_to_float(d):
    dollar = float(d[1:])
    return dollar

#it is assumed that the user will input in the "##%"" format
def percent_to_float(p):
    percent = float(p[:-1])/100
    return percent

main()