
fileName = input("Give a file name: ")

fileContent = input("Write something: ")

f = open(fileName, "a")
f.write(fileContent)
f.close()

print (f"Wrote {fileContent} to the file {fileName}")