#implementation of seasons exercise
import datetime
import sys
import re
import inflect 

def main():
    try:
        print(convert(input("Date of Birth: ")))
    except ValueError:
        sys.exit("Invalid Date")

def birth_date(day):
    #check if input is within range
    if re.search(r"^[\d]{4}-[\d]{2}-[\d]{2}$", day):
         return day.split("-")
    else:
        raise ValueError
    
def calculate(day):
    #get current date time
    b_day = datetime.date(int(day[0]), int(day[1]), int(day[2]))
    today = datetime.date.today()
    #min passed
    days = abs(today - b_day)
    minutes = days.days * 1440
    return minutes

def convert(day):
    day = birth_date(day)
    minutes = calculate(day)
    convertor = inflect.engine()
    converted = convertor.number_to_words(minutes)
    return converted.replace(" and ", " ")

if __name__ == "__main__":
        main()
