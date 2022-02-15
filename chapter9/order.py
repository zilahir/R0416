def getFile():
    try:
      file = open("words.txt", "r")
      return file
    except IOError:
      print ("There seems to be no file with that name.")
      return 0

def main():
    wordsFile = getFile()
    print ("Words in an alphabetical order:")
    for line in sorted(wordsFile.readlines()):
        print(line, end='')

if __name__ == "__main__":
    main()