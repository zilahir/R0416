def poweroftwo(num):
    result = 1
    for i in range(num):
        result *= 2
    print (f"The result is {result}")

def main():
    givenNumber = input("Give a number: ")
    poweroftwo(int(givenNumber))

if __name__ == "__main__":
    main()