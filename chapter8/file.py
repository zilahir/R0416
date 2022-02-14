def getFile(fileName):
    try:
      file = open(fileName, "r")
      return file
    except IOError:
      print ("There seems to be no file with that name.")
      return 0

def verifyFileContent(file):
    try:
        parsedNumber = int(file.read())
        return parsedNumber
    except Exception:
        print("The file contents were unsuitable.")

def main():
    fileName = input("Give the file name: ")
    file = getFile(fileName)
    if file:
        fileContent = verifyFileContent(file)
        if (fileContent):
            result = 1000 / fileContent
            print (f"The result was {result}")

if __name__ == "__main__":
    main()