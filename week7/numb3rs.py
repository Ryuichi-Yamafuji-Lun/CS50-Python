#implement numb3rs exercise
import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^(\d+)\.(\d+)\.(\d)+\.(\d)$", ip):
        #split the ip string
        ip_split = ip.split(".")
        #see if the ip follows the IPv4 address rules
        for num in ip_split:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False
    
if __name__ == "__main__":
    main() 