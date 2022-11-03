#implement outdated exercise
#month list
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#check that day and month is within range
def check(day, month, year):
    if day <= 31 and month <= 12:
        print(f"{year}-{month:02}-{day:02}")
        exit()
    

def main():
    while(True):
        try:
            date = input("Date: ").split()
            #check to see if input is month/date/year format
            if len(date) == 1:
                date = date[0].split("/")
                m = int(date[0])
                d = int(date[1])
                check(d, m, date[2])
            else:
                #check if month exist in the list
                if date[0] in month:
                    m = int(month.index(date[0])) + 1
                    d = int(date[1].replace(",",""))
                    check(d, m, date[2])
        except KeyError:
            pass

main()