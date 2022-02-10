print ("Calculator")

num1 = input("Give the first number: ")
num2 = input("Give the second number: ")

mathMethods = {
  "1": "+",
  "2": "-",
  "3": "*",
  "4": "/"
}

for key, value in mathMethods.items():
    text = f'({key}) {value}'
    print (text)

chosenMethod = input ("Please select something (1-4): ")

if (int(chosenMethod) >= 1 and int(chosenMethod) <= 4):
    if (chosenMethod == "1"):
        result = int(num1) + int(num2)
    elif (chosenMethod == "2"):
        result = int(num1) - int(num2)
    elif (chosenMethod == "3"):
        result = int(num1) * int(num2)
    elif (chosenMethod == "4"):
        result = int(num1) / int(num2)
    print (f"The result is: {result}")
else:
    print ("Selection was not correct.")
