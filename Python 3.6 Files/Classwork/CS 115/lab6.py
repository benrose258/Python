'''
Created on 2-27-17
@author: Ben Rose
Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose

CS115 - Lab 6 - Binary and Ternary conversions
'''
def isOdd(mynumber):
    '''Returns whether or not the integer argument is odd.'''
    '''Base-2 representation of 42: 101010'''
    if mynumber % 2 == 1:
        return True
    else:
        return False

def numToBinaryHelp(mynumber):
    if mynumber == 0:
        return ''
    else:
        if isOdd(mynumber) == True:
            return '1' + numToBinaryHelp(mynumber//2)
        else:
            return '0' + numToBinaryHelp(mynumber//2)

def reversal(mystring):
    if mystring == '':
        return ''
    else:
        return str(mystring[-1]) + reversal(mystring[:-1])

def numToBinary(mynumber):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    return reversal(numToBinaryHelp(mynumber))

def binaryToNum(mystring):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if mystring == '':
        return 0
    else:
        if mystring[0] == '1':
            return 2**(len(mystring)-1) + binaryToNum(mystring[1:])
        else:
            return binaryToNum(mystring[1:])

def increment(mystring):
    if mystring == '11111111':
        return '00000000'
    else:
        return howManyBits(numToBinary(binaryToNum(mystring) + 1))

def howManyBits(mystring):
    if len(mystring) == 8:
        return mystring
    elif len(mystring) > 8:
        return mystring[0:8]
    else:
        return howManyBits('0' + mystring)

def count(mystring, mynumber):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(mystring)
    return countHelp(mystring,mynumber)

def countHelp(mystring,mynumber):
    if mynumber == 0:
        return ''
    else:
        print(increment(mystring))
        return countHelp(increment(mystring),mynumber-1)

def zeroOrTwo(mynumber):
    if mynumber % 3 == 1:
        #If it is 1
        return 1
    elif mynumber % 3 == 2:
        #If it is 2
        return 2
    else:
        #If it is 0
        return 0

def numToTernaryHelp(mynumber):
    if mynumber == 0:
        return ''
    else:
        if zeroOrTwo(mynumber) == 1:
            return '1' + numToTernaryHelp(mynumber//3)
        elif zeroOrTwo(mynumber) == 2:
            return '2' + numToTernaryHelp(mynumber//3)
        else:
            return '0' + numToTernaryHelp(mynumber//3)

def numToTernary(mynumber):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    return reversal(numToTernaryHelp(mynumber))

def ternaryToNum(mystring):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if mystring == '':
        return 0
    else:
        if mystring[0] == '0':
            return ternaryToNum(mystring[1:])
        elif mystring[0] == '1':
            return 1 * 3**(len(mystring)-1) + ternaryToNum(mystring[1:])
        else:
            return 2 * 3**(len(mystring)-1) + ternaryToNum(mystring[1:])
