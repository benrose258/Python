'''
Created on Sep 10, 2017

@author: Ben Rose
'''
avogadrosNum = 6.022 * (10**23)

def sciFiNotation(number,exp):
    if 1 <= number < 10:
        return str(number) + ' * 10^'+str(exp)
    else:
        if number < 1:
            return sciFiNotation(number*10, exp - 1)
        else:
            return sciFiNotation(number/10, exp + 1)

#print(sciFiNotation(120, 0))
'''elementList format: element symbol, grams per mol, grams given'''

Cr = ['Cr',51.996,21.293]
S = ['S',32.06,41.559]
Pt = ['Pt',195.08,11.125]
Sn = ['Sn',118.71,87.009]
He = ['He',4.0026,541000]

def numAtoms(mylist):
    molarMass = mylist[2]/mylist[1]
    atoms = molarMass * avogadrosNum
    return str(sciFiNotation(atoms, 0))+' atoms of '+mylist[0]


print(numAtoms(Cr))
print(numAtoms(S))
print(numAtoms(Pt))
print(numAtoms(Sn))
print()
print(numAtoms(He))

'''atomsToMoles element list format: elemental symbol, given number of atoms'''
Ag = ['Ag',3.8*10**22]
def atomsToMoles(mylist):
    howManyMoles = mylist[1]/avogadrosNum
    return str(sciFiNotation(howManyMoles, 0))+' moles of '+mylist[0]

print()
print(atomsToMoles(Ag))
print()

Xe = ['Xe',131.29]
def atomToGrams(mylist):
    oneMol = mylist[1]*avogadrosNum
    return str(sciFiNotation(mylist[1]*1/avogadrosNum, 0))+' grams of '+mylist[0]

print(atomToGrams(Xe))
print()

'''numMoles element list format: element symbol, grams per mol, grams given'''

Cu = ['Cu',63.546,33.2]
def numMoles(mylist):
    molarMass = mylist[2]/mylist[1]
    return str(molarMass)+' moles of '+mylist[0]

print(numMoles(Cu))
print(sciFiNotation(294/avogadrosNum, 0))