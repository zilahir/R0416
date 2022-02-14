def checkPassword(password):
    hasNumbers = any(char.isdigit() for char in password)
    hasLetters = password.isdigit()
    if (hasNumbers == False and hasLetters == False):
        return False
    if (len(password) < 6):
        return False
    elif (hasNumbers == True and hasLetters == True):
        return False
    else:
        return True

def testme(stringToTest):
    isPasswordOk = checkPassword(stringToTest)
    return isPasswordOk
    