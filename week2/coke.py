#implementation of coke exercise
def main():
    due = int(input("Amount Due: "))
    while due != 0:
        price = int(input("Insert Coin: "))
        if due - price < 0:
            print(f"Change owed: {due}")
        elif price == 25:
            due -= 25
            print(f"Change owed: {due}") 
        elif price == 10:
            due -= 10
            print(f"Change owed: {due}") 
        elif price == 5:
            due -= 5
            print(f"Change owed: {due}") 
        else:
            print(f"Change owed: {due}") 

if __name__ == "__main__":
        main()