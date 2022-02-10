correctName = "John"
correctPassword = "ABC123"

givenName = input("Give name: ")

if givenName != correctName:
    print ("The given name is wrong.")
else:
    givenPassword = input("Give password: ")
    if (givenPassword != correctPassword):
        print ("The password is incorrect.")
    else:
        print ("Both inputs are correct!")