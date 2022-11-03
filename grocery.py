#implementation of grocery exercise
def main():
    #list for the grocery
    list = {}
    while(True):
        try:
            #input and capitilize all
            grocery = input().upper()
            #check if grocery is in list
            if grocery in list:
                list[grocery] += 1
            #if not then add the grocery
            else:
                list[grocery] = 1
        #control-d to print out values
        except EOFError:
            #itterate through key and value of list items an print. 
            for key, value in list.items():
                print(f"{value} {key}")
            exit()
main()