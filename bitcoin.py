#implementation of bitcoin.py
from pip._vendor import requests
import sys

#check if float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#check if command line argument is there
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
    
#check if command line arguement is a int
arg = sys.argv[1]
if isfloat(arg) != True:
    print("Command-line argument is not a number")
    sys.exit(1)

#find out much is n bitcoins
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total = bitcoin * float(arg)
    print(f"${total}")
except requests.RequestException:
    sys.exit(1)
