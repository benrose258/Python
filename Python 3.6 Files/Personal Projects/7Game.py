def contains(mystring, part):
    for index in mystring:
        if index == part:
            return True
    return False

def checkNumber(num):
    if num % 7 == 0:
        return "Multiple!"
    elif contains(str(num), '7') == True:
        return "Contains a 7!"
    else:
        return num

def SevenGame():
    print('Would you like to display odds(o), evens(e), or all?')
    initialize = input('Please type o, e, or any key for all numbers> ')
    print()
    howmanynums = int(input('How many numbers would you like to check? '))
    if initialize == 'o':
        print()
        for number in range(howmanynums):
            number += 1
            if number % 2 == 0:
                print()
            else:
                print(checkNumber(number))
    elif initialize == 'e':
        for number in range(howmanynums):
            number += 1
            if number % 2 == 0:
                print(checkNumber(number))
            else:
                print()
    else:
        for number in range(howmanynums):
            number += 1
            print(checkNumber(number))

SevenGame()
