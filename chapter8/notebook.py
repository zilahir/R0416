import time

class NoteBook:
    def __init__(self):
        self.noteBook = None
        self.fileName = None
    
    def openNoteBook(self, fileName):
        try:
            noteBook = open(fileName, "r")
            self.noteBook = noteBook
            self.fileName = fileName
        except IOError:
            if (fileName == "notebook.txt"):
                print("No default notebook was found, created one.")
            else:
                print("No notebook with that name detected, created one.")
            file = open(fileName, "w+")
            self.noteBook = file
            self.fileName = fileName

    def writeNoteBook(self, newNote):
        self.noteBook.write(f"{newNote}:::{getCurrentDate()}\r\n")
    
    def readNoteBook(self):
        print (self.noteBook.read())
    
    def emptyNoteBook(self):
        self.noteBook = open(self.fileName, "w")
        self.noteBook.write("\r\n")
    
    def closeNoteBook(self):
        self.noteBook.close()
    
    def currentNoteBook(self):
        return self.fileName


def getCurrentDate():
    return time.strftime("%X %x")

noteBookMethods = {
  "1": "Read the notebook",
  "2": "Add note",
  "3": "Empty the notebook",
  "4": "Change the notebook",
  "5": "Quit",
}

def askForNoteCommand():
    for key, value in noteBookMethods.items():
        text = f'({key}) {value}'
        print (text)
    noteCommand = input("Please select one: ")
    return noteCommand

def handleCommand(command, noteBook):
    if command == "1":
        noteBook.readNoteBook()
    if command == "2":
        newNote = input("Write a new note: ")
        noteBook.writeNoteBook(newNote)
    if command == "3":
        noteBook.emptyNoteBook()
    if command == "4":
        newFileName = input("Give the name of the new file: ")
        noteBook.openNoteBook(newFileName)



def main():
    chsoenCommand = None
    noteBook = NoteBook()
    noteBook.openNoteBook("notebook.txt")
    while (chsoenCommand != "5"):
        print(f"Now using file {noteBook.currentNoteBook()}")
        chsoenCommand = askForNoteCommand()
        handleCommand(chsoenCommand, noteBook)

    if (chsoenCommand == "5"):
        noteBook.closeNoteBook()
        print ("Notebook shutting down, thank you.")


if __name__ == "__main__":
    main()