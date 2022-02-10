
from curses.ascii import isalnum


inputFile = open('strings.txt', 'r')

count = 0

def checkLine(lineString):
    if (lineString.isalnum()):
        print (f'{lineString} was ok.')
    else:
        print (f'{lineString} was invalid.')


 
while True:
    count += 1
    line = inputFile.readline()
    if not line:
        break
    checkLine(line.strip())
 
inputFile.close()