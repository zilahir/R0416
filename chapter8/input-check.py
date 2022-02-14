givenNumber = input("Give a numeric value: ")

try:
    parsedNumber = int(givenNumber)
    print("The input was suitable!")

except Exception:
    print("The input was malformed.")