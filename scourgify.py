#implement scourgify exercise
import sys

def main():
    copy = []
    try:
        file1, file2 = file_check()
        with open(file1) as file:
            for line in file:
               copy.append(line)
        
    except FileNotFoundError:
        sys.exit("File not found")

#check if command line meets requirements
def file_check():
    if len(sys.argv) == 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        return file1, file2
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()