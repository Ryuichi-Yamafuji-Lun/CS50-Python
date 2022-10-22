#implementation of einstein exercise
def calculator(mass):
    return(int(mass) * (300000000*300000000))

def main():
    mass = input("m: ")
    energy = calculator(mass)
    print(energy)

main()