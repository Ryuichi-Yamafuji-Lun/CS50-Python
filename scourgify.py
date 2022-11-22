#implement scourgify exercise
import sys

def main():
    copy = []
    try:
        #read file
        file1, file2 = file_check()
        with open(file1) as file:
            for line in file:
               copy.append(line)
        copy = split(copy)
        #write to second file
        with open(file2, "w") as file:
            for line in copy:
                file.write(", ".join(line))

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

#split first and last name
def split(copy):
    copy.pop(0)
    new_cpy = [line.replace('"', '').split(",") for line in copy]
    for line in new_cpy:
        temp = line[1].replace(" ","")
        line[1] = line[0]
        line[0] = temp
    return new_cpy
        

if __name__ == "__main__":
    main()