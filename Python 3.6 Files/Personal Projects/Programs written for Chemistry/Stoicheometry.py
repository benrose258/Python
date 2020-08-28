'''
Created on Sep 23, 2017

@author: Ben Rose
'''

class Element(object):
    '''Element symbol (eleSym) (string)
       Subscript (eleSub): (integer)
       Molar Mass of the element (molMass)
       All fields are private.'''
    def __init__(self,eleSym,eleSub,molMass):
        self.__eleSym = eleSym
        self.__eleSub = eleSub
        self.__molMass = molMass

    def eleSym(self):
        return self.__eleSym

    def eleSub(self):
        return self.__eleSub

    def molMass(self):
        return self.__molMass

    def eleSym(self,eleSym):
        self.__eleSym = eleSym

    def eleSub(self,eleSub):
        self.__eleSub = eleSub

    def molMass(self,molMass):
        self.__molMass = molMass

    def get_mass(self):
        '''Returns the molar mass of the element * the subscript (the subscript represents
        the number of moles of the element given'''
        return self.__eleSub * self.__molMass

    def __add__(self, other):
        '''Adds elements based on their mass and subscripts.'''
        if type(other) != Element:
            return other + self.get_mass()
        else:
            return self.get_mass() + other.get_mass()

    def __mul__(self,number):
        return number * self.get_mass()

    def __str__(self):
        return 'Element symbol: '+self.__eleSym + '\n' + \
            'Subscript: '+str(self.__eleSub)+ '\n' + \
            'Molar Mass: '+str(self.__molMass)

def getElementData():
    '''
       Contains Four Functions:

       getSymbol: Gets element's symbol

       getSubscript: Gets the element's subscript

       getMolarMass: Gets the mass of one mole of the element

       confirmInfo: Confirming the symbol, subscript, and molar mass,
       and correcting them if they are incorrect. Upon
       confirmation, this function prints the information to be read
       by the element function (above)
    '''
    def getSymbol():
        prompt = input("Please input symbol of element> ")
        return prompt
    def getSubscript():
        prompt = float(input("Please input subscript of element> "))
        if int(prompt) == prompt:
            return int(prompt)
        return prompt
    def getMolarMass():
        prompt = float(input("Please input molar mass of element> "))
        return prompt
    def confirmInfo(mySymbol,mySubscript,myMolarMass):
        print()
        print('1. Element Symbol: '+mySymbol)
        print('2. Subscript: '+str(mySubscript))
        print('3. Molar Mass: '+str(myMolarMass))
        print('''
This is the information provided. If there
is an issue, type the corresponding number
you'd like to replace. Otherwise, type Y.''')
        print()
        prompt = input('Please input 1, 2, 3, or Y> ')
        print()
        if prompt == '1':
            mySymbol = getSymbol()
        elif prompt == '2':
            mySubscript = getSubscript()
        elif prompt == '3':
            myMolarMass = getMolarMass()
        elif prompt == 'Y' or prompt == 'y':
            print('Your information is confirmed.')
            print('The code for your element is below:')
            print()
            return mySymbol+str(mySubscript)+' = ''Element(\''+mySymbol+'\','+str(mySubscript)+','+str(myMolarMass)+')'
        else:
            print('Error: Please enter one of the provided inputs.')
        print()
        return confirmInfo(mySymbol,mySubscript,myMolarMass)
    mySymbol = getSymbol()
    mySubscript = getSubscript()
    myMolarMass = getMolarMass()
    elementData = confirmInfo(mySymbol,mySubscript,myMolarMass)
    print(elementData)
    return elementData

if __name__ == '__main__':
    getElementData()
