uppercaseLetters = ("A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def threeUp3Digits():
    finallist = []
    for letter1 in uppercaseLetters:
        for letter2 in uppercaseLetters:
            for letter3 in uppercaseLetters:
                for digit1 in digits:
                    for digit2 in digits:
                        for digit3 in digits:
                            finallist.append([letter1,letter2,letter3,digit1,digit2,digit3])
    return len(finallist)
