def tester(givenstring = "Too short"):
    if len(givenstring) < 10:
        print ("Too short")
    else:
        print (givenstring)
        if (givenstring.find("X") != -1):
                print ("X spotted!")

    

def main():
    userInput = None
    while (userInput != "quit"):
        userInput =input("Write something (quit ends): ")
        if (userInput != "quit"):
            tester(userInput)

if __name__ == "__main__":
    main()