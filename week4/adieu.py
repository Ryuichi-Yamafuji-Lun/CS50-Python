#implementation of adieu letters
def main():
    names = []
    i = 0
    while(True):
        try:
            name = input("Name: ")
            if (name != ""):  
                names.append(name)
        
        except EOFError:
            print("\n" + "Adieu, adieu, to ", end="")
            while i < len(names) - 1:
                print(names[i] + ", ", end="")
                i += 1
            print("and " + names[i])
            exit()
    

main()