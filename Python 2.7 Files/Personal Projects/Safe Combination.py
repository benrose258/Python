import random

def safecombo():
    #initialization
    #combolength and keypad takes user input and sets it to the safe combination length
    combolength = input("What is the safe combination length? ")
    keypad = input("How many possible numbers are available? ")
    yesornolimit = input("Would you like an attempt limit? True or False: ")
    if yesornolimit == True:
        attemptlimit = input("How many attempts do you have? ")
    else:
        attemptlimit = False
    #Makes safe combination
    combination = makeSafeCombination(combolength,keypad)
    myguess = []
    displayBar = []
    round = 1
    while myguess != combination:
        if attemptlimit!=False:
            if attemptlimit>=round:
                #get myguess from player
                print "Enter your combination for attempt", round,"..."
                myguess = readMyGuess(combination,keypad)
                displayBar.append(myguess)
                #compares myguess with the combination and gives feedback
                if myguess != combination:
                    printDisplayBar(displayBar,combination,keypad)
                round = round + 1
            else:
                print ""
                return "Game over. You lose. Please try again."
        else:
            #get myguess from player
                print "Enter your combination for attempt ", round,"..."
                myguess = readMyGuess(combination,keypad)
                displayBar.append(myguess)
                #compares myguess with the combination and gives feedback
                if myguess != combination:
                    printDisplayBar(displayBar,combination,keypad)
                round = round + 1
    #player guessed the safe combination
    #give feedback
    if round==1:
        print "Excellent. You cracked the safe on the first try."
    else:
        print "You broke the safe in", round-1,"attempts."

def makeSafeCombination(combolength,keypad):
    combination = []
    for index in range(combolength):
        combination.append(random.choice(range(keypad)))
    return combination

def getMyGuess(currentplace,keypad):
    print "Enter a number from",range(keypad),"for position",currentplace, "in the combination..."
    number_entered = input()
    return number_entered

def readMyGuess(combolength,keypad):
    myguess = []
    for currentplace in range(len(combolength)):
        currentplace=currentplace+1
        myguess.append(getMyGuess(currentplace,keypad))
    return myguess

def findCorrectNumbers(myguess,combination,keypad):
    found = [0] * keypad
    score = ["placeholder"] * len(combination)
    for index in range(len(myguess)): #Find the correct numbers first!
        if myguess[index] == combination[index]:
            found[myguess[index]] = found[myguess[index]]+1
            score[index]="Perfect"
    return [score, found]

def crackedStatus(myguess,combination,keypad):
    currentStatus = findCorrectNumbers(myguess,combination,keypad)
    score = currentStatus[0]
    found = currentStatus[1]
    for index in range(len(myguess)):
        if myguess[index] == combination[index]:
            pass
        #^^Handled in findCorrectNumbers
        elif counter(myguess[index],myguess)<=counter(myguess[index],combination):
            found[myguess[index]]=found[myguess[index]]+1
            score[index]="white"
        else:
            #^^counter(myguess[index],myguess)>counter(myguess[index],combination)
            found[myguess[index]] = found[myguess[index]]+1
            if found[myguess[index]]<=counter(myguess[index],combination):
                #We haven't found all of them yet
                score[index]="white"
            else:
                score[index]="empty"
    return score

def counter(x,mylist):
    count=0
    for y in mylist:
        if x == y:
            count = count+1
    return count

def printDisplayBar(displayBar,combination,keypad):
    print("")
    print("Your attempted combination:")
    for myguess in displayBar:
        print(myguess, crackedStatus(myguess,combination,keypad))
