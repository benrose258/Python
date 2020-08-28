'''
Created on Mar 22, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''

def bitFlip(mystring):
    '''Flips each bit'''
    if mystring == '':
        return ''
    else:
        if mystring[0] == '0':
            return '1' + bitFlip(mystring[1:])
        else:
            return '0' + bitFlip(mystring[1:])
        
def TcToNum(mystring):
    '''Converts a binary string to its two's compliment representation.'''
    plusZeros = '0' * 8 + mystring
    updatedString = plusZeros[-8:]
    if updatedString[0] == '0':
        return binaryToNum(updatedString)
    else:
        return -1 * (binaryToNum(bitFlip(updatedString)) + 1)

def NumToTc(mynumber):
    '''Converts a number in two's compliment into its binary string.'''
    if mynumber < -128 or mynumber >= 128:
        return 'Error'
    else:
        binaryRep = '0'*8 + numToBinary(abs(mynumber))
        if mynumber >= 0:
            return binaryRep[-8:]
        else:
            binaryRepNeg = numToBinary(binaryToNum(bitFlip(binaryRnep[-8:])) + 1)
            return binaryRepNeg[-8:]

def isOdd(mynumber):
    '''Returns whether or not the integer argument is odd.'''
    '''Base-2 representation of 42: 101010'''
    if mynumber % 2 == 1:
        return True
    else:
        return False

def numToBinaryHelp(mynumber):
    '''Does computations for numToBinary'''
    if mynumber == 0:
        return ''
    else:
        if isOdd(mynumber) == True:
            return '1' + numToBinaryHelp(mynumber//2)
        else:
            return '0' + numToBinaryHelp(mynumber//2)

def reversal(mystring):
    '''Reverses a string'''
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