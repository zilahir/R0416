import math

mathMethods = {
  "1": "+",
  "2": "-",
  "3": "*",
  "4": "/",
  "5": "sin(number1/number2)",
  "6": "cos(number1/number2)",
  "7": "Change numbers",
  "8": "Quit"
}

result = 0

def validateInput(input):
    try:
        return int(input) > 0
    except ValueError:
        return False

def getNumber(
    prompt="Give a number: ",
    validator=lambda x: True,
    error_message="This input is invalid.",
    ):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(error_message)

def askForNumbers():
    firstNumber = getNumber("Give a number: ", validateInput)
    secondNumber = getNumber("Give a number: ", validateInput)
    
    return [int(firstNumber), int(secondNumber)]

def askForSelection(givenNumbers):
    for key, value in mathMethods.items():
        text = f'({key}) {value}'
        print (text)
    print (f"Current numbers: {givenNumbers[0]} {givenNumbers[1]}")
    chosenMethod = input ("Please select something (1-6): ")
    return chosenMethod



numbers = []
print ("Calculator")
numbers = askForNumbers()


chosenMethod = None
while chosenMethod != str(8):
    chosenMethod = askForSelection(numbers)
    if (chosenMethod == "1"):
        result = numbers[0] + numbers[1]
        print (f"The result is: {result}")
    elif (chosenMethod == "2"):
        result = numbers[0] - numbers[1]
        print (f"The result is: {result}")
    elif (chosenMethod == "3"):
        result = numbers[0] * numbers[1]
        print (f"The result is: {result}")
    elif (chosenMethod == "4"):
        result = numbers[0] / numbers[1]
        print (f"The result is: {result}")
    elif (chosenMethod == "5"):
        partial = numbers[0] / numbers[1]
        result = math.sin(partial)
        print (f"The result is: {result}")
    elif (chosenMethod == "6"):
        partial = numbers[0] / numbers[1]
        result = math.cos(partial)
        print (f"The result is: {result}")
    elif (chosenMethod == "7"):
        numbers = askForNumbers()


if chosenMethod == str(8):
    print ("Thank you!")



