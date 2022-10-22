#faces implementation smile and frowns
#converter
def convert(message):
    message = message.replace(":)","🙂")
    message = message.replace(":(","🙁")
    return message
    
#main
def main():
    message = input()
    message = convert(message)
    print(message)

main()