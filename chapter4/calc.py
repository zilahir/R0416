userInput = input("Give a number: ")

userInputInt = int(userInput)

sumOfNums = 0

for index in range(userInputInt):
    sumOfNums = sumOfNums + index

print (f"The sum was: {sumOfNums}")