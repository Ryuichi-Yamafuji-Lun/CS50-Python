#implement lines exercise
import sys
def main():
    lines = []
    counter = 0
    try:
        py_file = check()
        with open(py_file) as file:
            for line in file:
                lines.append(line.lstrip())
                
        while '' in lines:
            lines.remove('')

        for line in lines:
            if line.startswith("#") == False:
                counter += 1
        print(counter)           
    except FileNotFoundError:
        sys.exit("File does not exist")


def check():
    #check if command-line input is correct
    if len(sys.argv) == 2:
        file = sys.argv[1]
        if file[-3:] == ".py":
            return file
        else:
            sys.exit("Not a Python File")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()