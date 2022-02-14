import time

def getFile(method):
    return open('notebook.txt', method)

def getCurrentDate():
    return time.strftime("%X %x")

noteBookMethods = {
  "1": "Read the notebook",
  "2": "Add note",
  "3": "Empty the notebook",
  "4": "Quit",
}

def askForNoteCommand():
    for key, value in noteBookMethods.items():
        text = f'({key}) {value}'
        print (text)
    noteCommand = input("Please select one: ")
    return noteCommand

def handleCommand(command):
    if command == "1":
        noteBook = getFile('r')
        print (noteBook.read())
    if command == "2":
        newNote = input("Write a new note: ")
        noteBook = getFile('a')
        noteBook.write(f"{newNote}:::{getCurrentDate()}\r\n")
    if command == "3":
        noteBook = getFile('w')
        noteBook.write("\r\n")
        noteBook.close()
        print ("Notes deleted.")


chsoenCommand = None
while (chsoenCommand != "4"):
    chsoenCommand = askForNoteCommand()
    handleCommand(chsoenCommand)

if (chsoenCommand == "4"):
    print ("Notebook shutting down, thank you.")