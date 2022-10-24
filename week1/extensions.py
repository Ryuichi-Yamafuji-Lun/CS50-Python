#implementation of the extension exercise
def main():
    File = input("File name: ")
    extension = File.split(".")
    if len(extension) != 2:
        print("application/octet-stream")
        return 0
    #get extension
    ext = extension[1]
    if ext == "gif":
        print("image/gif")
    elif ext == "jpg":
        print("image/jpg")
    elif ext == "jpeg":
        print("image/jpeg")
    elif ext == ("png"):
        print("image/png")
    elif ext == "pdf":
        print("image/pdf")
    elif ext == "txt":
        print("image/txt")
    elif ext == "zip":
        print("image/zip")
    else:
        print("application/octet-stream")
main()