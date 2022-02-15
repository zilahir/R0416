# -*- coding: cp1252 -*-
import time
import pickle

class NoteBook:
    def __init__(self):
        self.noteBook = None
        self.fileName = None
        self.notes = []
    
    def openNoteBook(self, fileName):
        try:
            noteBook = open(fileName, "rb+")
            self.noteBook = noteBook
            self.fileName = fileName
            self.notes = pickle.load(self.noteBook)
        except IOError:
            print("No default notebook was found, created one.")
            file = open(fileName, "wb")
            self.noteBook = file
            self.fileName = fileName

    def writeNoteBook(self, newNote):
        note = f"{newNote}:::{getCurrentDate()}"
        self.notes.append(note)
    
    def getNoteById(self, noteId):
        return self.notes[noteId]
    
    def modifyNote(self, indexToModify):
        if (int(indexToModify) <= len(self.notes)):
            thisNote = self.getNoteById(int(indexToModify))
            print (thisNote)
            modifiedNote = input("Give the new note: ")
            self.notes[int(indexToModify)] = f"{modifiedNote}:::{getCurrentDate()}"
    
    def deleteNote(self, indexToDelete):
        if (int(indexToDelete) <= len(self.notes)):
            print (f"Deleted note {self.getNoteById(int(indexToDelete))}")
            self.notes.pop(int(indexToDelete))
    
    def readNoteBook(self):
        print(*self.notes, sep = "\n")
    
    def emptyNoteBook(self):
        self.notes = []
    
    def updateNoteBook(self):
        pickle.dump(self.notes, self.noteBook)
    
    def getNotes(self):
        return self.notes

    
    def currentNoteBook(self):
        return self.fileName

    def closeNoteBook(self):
        self.updateNoteBook()
        self.noteBook.close()


def getCurrentDate():
    return time.strftime("%X %x")

noteBookMethods = {
  "1": "Read the notebook",
  "2": "Add note",
  "3": "Edit a note",
  "4": "Delete a note",
  "5": "Save and quit",
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
        print (f"The list has {len(noteBook.getNotes())} notes.")
        indexToModify = input("Which of them will be changed?: ")
        noteBook.modifyNote(indexToModify)
    if command == "4":
        print (f"The list has {len(noteBook.getNotes())} notes.")
        indexToModify = input("Which of them will be deleted?: ")
        noteBook.deleteNote(indexToModify)



def main():
    chsoenCommand = None
    noteBook = NoteBook()
    noteBook.openNoteBook("notebook.dat")
    while (chsoenCommand != "5"):
        chsoenCommand = askForNoteCommand()
        handleCommand(chsoenCommand, noteBook)

    if (chsoenCommand == "5"):
        noteBook.readNoteBook()
        noteBook.closeNoteBook()
        print ("Notebook shutting down, thank you.")


if __name__ == "__main__":
    main()