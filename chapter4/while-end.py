
def askUser():
    userInput = input("Write something: ")
    return userInput

quitWord = "quit"
userInput = None

while userInput != quitWord:
    userInput = askUser()
    if (userInput != quitWord):
        print (userInput)

if (userInput == quitWord):
    print ("Bye bye!")