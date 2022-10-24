#implement meal time exercise
def main():
    time = input("What time is it? ")
    x = convert(time)

    #check time
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")
    else:
        return 0
    
def convert(time):
    min_per_hour = 60
    time = time.split(":")
    min = float(int(time[1]) / min_per_hour)
    hours = float(int(time[0]) + min)
    return hours

if __name__ == "__main__":
    main()