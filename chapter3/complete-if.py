
chosenNumber = input("Select a number (1-3): ")

numToString = {
  "1": "one",
  "2": "two",
  "3": "three"
}

if int(chosenNumber) >= 1 and int(chosenNumber) <= 3:
    formatted = f'You selected {numToString[chosenNumber]}.'
    print (formatted)