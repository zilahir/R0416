
class ShoppingList:
    def __init__(self):
        self.shoppingList = []
        self.methods = {
            "1": "Add or\r\n",
            "2": "Remove items or\r\n",
            "3": "Quit?: "
        }
    
    def printShoppingList(self):
        for listItem in self.shoppingList:
            print (listItem)
    
    def deleteItemFromShoppingList(self):
        itemToDelete = input("Which item is deleted?: ")
        if int(itemToDelete) > len(self.getShoppingListItems()) - 1:
            print ("Incorrect selection.")
        else:
            self.shoppingList.pop(int(itemToDelete))
    
    def getShoppingListItems(self):
        return self.shoppingList
    
    def addToShoppingList(self):
        newItem = input("What will be added?: ")
        self.shoppingList.append(newItem)

    def getMethods(self):
        text = ""
        for key, value in self.methods.items():
            text += f'({key}){value}'
        return text

def validateInput(input):
    try:
        return int(input) > 0 and int(input) < 4
    except ValueError:
        return False

def getCommand(
    methods,
    validator=lambda x: True,
    error_message="Incorrect selection.",
    ):
    while True:
        value = input(f"Would you like to\r\n{methods}")
        if validator(value):
            return value
        print(error_message)

def main():
    shoppingList = ShoppingList()
    methods = shoppingList.getMethods()
    chosenMethod = None
    while chosenMethod != "3":
        chosenMethod = getCommand(methods, validateInput)
        if (chosenMethod == "1"):
            shoppingList.addToShoppingList()
        if (chosenMethod == "2"):
            print (f"There are {len(shoppingList.getShoppingListItems())} items in the list.")
            shoppingList.deleteItemFromShoppingList()


    if (chosenMethod == "3"):
        print ("The following items remain in the list:")
        shoppingList.printShoppingList()

if __name__ == "__main__":
    main()
