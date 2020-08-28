'''
Created on Sep 10, 2017

@author: Ben Rose
'''
isotopeList = [[['Br-81',80.916,49.31],['Br-79',78.918,50.69]] , [['Cl-37',36.966,24.23],['Cl-35',34.969,75.77]]]

def printSums(mylist):
    brList = mylist[0]
    clList = mylist[1]
    for brIso in brList:
        for clIso in clList:
            print(brIso[0]+' + '+clIso[0]+' : '+str(brIso[1]+clIso[1])+' amu')
            print()
    return ""

def calcPercent(number,percentage):
    return number * (percentage/100)

print(printSums(isotopeList))

def printAbundance(mylist):
    brList = mylist[0]
    clList = mylist[1]
    for brIso in brList:
        for clIso in clList:
            print(brIso[0]+' + '+clIso[0]+' : '+str(calcPercent(brIso[2],clIso[2]))+' %')
            print()
    return ""

print()
print()
print()
print(printAbundance(isotopeList))
