#playback speed implementation
import re
def main():
    play = input().strip()
    print(re.sub(" ", "...", play))

main()