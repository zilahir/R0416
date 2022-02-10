def checkIfOddOrEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

num1 = input("Give a number: ")
num2 = input("Give another number: ")

if checkIfOddOrEven(int(num1)) and checkIfOddOrEven(int(num2)):
    print ("Both numbers are even.")
elif checkIfOddOrEven(int(num1)) and not checkIfOddOrEven(int(num2)):
    print ("One of the numbers is even.")
elif not checkIfOddOrEven(int(num1)) and not checkIfOddOrEven(int(num2)):
    print ("Both numbers are odd.")
