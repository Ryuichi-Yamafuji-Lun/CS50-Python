#implementation of working exercise
import re

def main():
    print(convert(input("Hours: ")))

def convert(hours):
   if re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A|P]M)$", hours):
          #split input
          hours_split = hours.split(" ")
          #convert
          start_time = convert_time(hours_split, 1)
          end_time = convert_time(hours_split, 4)

          return start_time + " to " + end_time    
   else:
        raise ValueError

def convert_time(hours_split, x):
     if hours_split[x] == "AM":
          if re.search(r":", hours_split[x - 1]):
               hour, min = hours_split[x - 1].split(":")
               if int(hour) < 10:
                    time = "0" + hours_split[x - 1]
               else:
                    time = hours_split[x - 1] + ":" + min
          else:
               if int(hours_split[x - 1]) < 10:
                    time = "0" + hours_split[x - 1] + ":00" 
               else:
                    time = hours_split[x - 1] + ":00"
     else:
          #PM
          if re.search(r":", hours_split[x - 1]):
               hour, min = hours_split[x - 1].split(":")
               hour = str(int(hour) + 12)
               time = hour + ":" + min
          else:
               hour = str(int(hours_split[x - 1]) + 12)
               time = hour + ":00"      
     return time

if __name__ == "__main__":
        main()