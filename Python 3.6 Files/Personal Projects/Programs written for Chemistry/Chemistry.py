#Chemistry
from symbol import subscript
from pip._vendor.packaging.markers import Variable
avogadrosNum = 6.022 * (10**23)

def getElementData():
    #Get Element Data function
    getElement = input("Please enter the element letter> ")
    getMass = input("Please enter the element's molar mass> ")
    return [getElement,getMass]

def getElementList(currentList):
    keepgoing = None
    elements = currentList
    while keepgoing != "yes":
        getElement = input("Please enter the element letter> ")
        getMass = float(input("Please enter the element's molar mass> "))
        elements.append([getElement,getMass])
        promptUser = input("done? type yes if you are ")
        keepgoing = promptUser
    return elements

def getMole(elements):
    multiples = []
    counter = 0
    while len(elements) != len(multiples):
        molPrompt = int(input('how many moles of '+elements[counter][0]+' are present?'))
        counter += 1
        multiples.append(molPrompt)
    finallist = []
    for item in range(len(elements)):
        finallist.append([elements[item][0],elements[item][1],multiples[item]])
    return finallist

def sciFiNotation(number,exp):
    if 1 <= number < 10:
        return str(number) + ' * 10^'+str(exp)
    else:
        if number < 1:
            return sciFiNotation(number*10, exp - 1)
        else:
            return sciFiNotation(number/10, exp + 1)

def howMany():
    elements = getElementList([])
    newList = getMole(elements)
    totalMass = 0
    for element in newList:
        totalMass += (element[1]*element[2])
    print("Total Molar Mass: "+str(totalMass))
    massGiven = float(input("How many grams are given?"))
    for element in newList:
        print("Element: "+element[0])
        print('Molar Mass: '+str(element[1]))
        print("Moles: "+str(element[2]))
        print("Mass %: "+str(100*(element[1]*element[2])/totalMass))
        print()
    return 'Total Mass: '+str(totalMass)

def getPercent(elements):
    percents = []
    counter = 0
    while len(elements) != len(percents):
        getPercent = float(input('what percent of '+elements[counter][0]+' is present?'))
        counter += 1
        percents.append(getPercent)
    finallist = []
    for item in range(len(elements)):
        finallist.append([elements[item][0],elements[item][1],percents[item]])
    return finallist

def pComp():
    #Percent Composition
    elements = getElementList([])
    elePercents = getPercent(elements)
    getGiven = float(input('How many grams are provided?'))
    givenGrams = getGiven
    for element in elePercents:
        massAvailable = ((element[2]/100)*givenGrams)
        print("Element: "+element[0])
        print("Mass %: "+str(element[2]))
        print('Moles: '+str(massAvailable/element[1]))
        print("Grams per mol: "+str(element[1]))
        print()
    return 'exit'
