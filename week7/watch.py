#implementation of watch youtube exercise
import re

def main():
    print(parse(input("HTML: ")))

def parse(html):
    html = re.search(r'src="(.*?)"', html)
    html = "https://youtu.be/"+ html[0].rsplit('/',1)[1].replace('"','')
    return html

if __name__ == "__main__":
        main()