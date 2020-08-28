'''
Created on Mar 20, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''

def numToBaseB(mynumber,baseunit):
    '''Returns the reversed string of numToBaseBHelp. It is reversed to put it in the correct order. If the number is 0, however, it returns the
       string 0.'''
    if mynumber == 0:
        return '0'
    else:
        return reversal(numToBaseBHelp(mynumber,baseunit))

def zeroOrOther(mynumber,baseunit):
    '''Using the baseunit, this function outputs a string containing the number to be used in creation of the numToBaseB function.'''
    return str(mynumber % baseunit)

def reversal(mystring):
    '''Reverses a string.'''
    if mystring == '':
        return ''
    else:
        return str(mystring[-1]) + reversal(mystring[:-1])

def numToBaseBHelp(mynumber,baseunit):
    '''The brains of the numToBaseB function. Converts a non-negative integer to a string of base baseunit.'''
    if mynumber == 0:
        return ''
    else:
        return zeroOrOther(mynumber,baseunit) + numToBaseBHelp(mynumber//baseunit,baseunit)

def baseBToNum(mystring,baseunit):
    '''Converts a provided string and the base unit it is in and converts it to its corresponding number in base 10.'''
    if mystring == '':
        return 0
    else:
        return int(mystring[0]) * baseunit**(len(mystring)-1) + baseBToNum(mystring[1:],baseunit)

def baseToBase(baseunit1,baseunit2,mystring):
    '''Function will take in the unit that the original string is written in, the unit that the base1string, labeled mystring, will be converted to, and
       the string to be converted and will output the mystring in the baseunit2 base value.'''
    if mystring == '':
        return ''
    else:
        return numToBaseB(baseBToNum(mystring,baseunit1),baseunit2)

def add(binarystring1,binarystring2):
    '''Adds Binary String 1 and Binary String 2 and returns the sum in binary.'''
    return numToBaseB(baseBToNum(binarystring1,2) + baseBToNum(binarystring2,2),2)

FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def addB(binarystring1,binarystring2):
    '''Sets up base cases for: 1. if both strings are initially empty, then return 0. Then, if the first string is initially empty,
       return the second string. Then if the second string is initially empty, return the first string. Then if the two are unequal in
       length, then add zeros to the shorter string until the lengths of the two strings are equal. Now that both are equal in length
       and we know they were not initially empty, we can move to the helper function, and this will return the result of the helper.'''
    if binarystring1 == '' and binarystring2 == '':
        return '0'
    elif binarystring1 == '':
        return binarystring2
    elif binarystring2 == '':
        return binarystring1
    elif len(binarystring1) > len(binarystring2):
        howManyZeros = len(binarystring1) - len(binarystring2)
        addedZeros = '0' * howManyZeros
        return addB(binarystring1,addedZeros + binarystring2)
    elif len(binarystring2) > len(binarystring1):
        howManyZeros = len(binarystring2) - len(binarystring1)
        addedZeros = '0' * howManyZeros
        return addB(addedZeros + binarystring1, binarystring2)
    else:
        return addBHelper(binarystring1,binarystring2,'0')

def addBHelper(binarystring1,binarystring2,carriedBit):
    '''Resuming from where the addB left off, this function, starting with zero as the carried bit (as we aren't carrying any numbers
       when there werent any to carry from), using the rightmost bit (least significant bit) from both strings and the current carried bit,
       we look in the FullAdder dictionary (shown above) and add the corresponding sum bit and use the carry bit in our recursive call of the
       function. We have two base cases: the first if we are still carrying a one and the second if we are not. If we are carrying a 1, we
       add that to the beginning of our binary sum string and return the new sum string. If not, we just return an empty string, thereby
       returning the binary sum as is.'''
    if binarystring1 == '' and carriedBit == '1':
        return '1'
    elif binarystring1 == '':
        return ''
    else:
        sumBit, carriedBit = FullAdder[(binarystring1[-1],binarystring2[-1],carriedBit)]
        return addBHelper(binarystring1[:-1], binarystring2[:-1], carriedBit) + sumBit
