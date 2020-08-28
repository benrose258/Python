'''
Created on 3/6/17
@authors: Ben Rose
Pledge: We pledge our honor that we have abided by the Stevens Honor System. -Ben Rose
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5
# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1
# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def isOdd(mynumber):
    '''Returns whether or not the integer argument is odd.'''
    '''Base-2 representation of 42: 101010'''
    if mynumber % 2 == 1:
        return True
    else:
        return False
def numToBinaryHelp(mynumber):
    '''A non-reversed form of numToBinary (essentially the brains of it).'''
    if mynumber == 0:
        return ''
    else:
        if isOdd(mynumber) == True:
            return '1' + numToBinaryHelp(mynumber//2)
        else:
            return '0' + numToBinaryHelp(mynumber//2)
def reversal(mystring):
    '''Reverses strings.'''
    if mystring == '':
        return ''
    else:
        return str(mystring[-1]) + reversal(mystring[:-1])
def numToBinary(mynumber):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer mynumber.
    If mynumber is 0, the empty string is returned.'''
    return reversal(numToBinaryHelp(mynumber))
#lookingTo is the number, either zero or one, that we are going to search until. At the beginning we are counting how many zeros until
#the first 1. Then lookingTo would equal 1 as we are counting how many zeros until the first 1.
def compress(mystring):
    '''Sets up the main part of the function. It creates the variable lookingTo, which will alter between zero and one depending on which
    number we will stop searching at. Ex. lookingTo = 1. 000001 will return the number of zeros until the 1.'''
    lookingTo = 1
    return compressHelp(mystring,lookingTo)
def compressHelp(mystring,lookingTo):
    '''Using lookingTo, compressHelp essentially searches the string for the numbers of zeros and ones and returns them
    in the required iteration using the helper functions below.'''
    if mystring == '':
        return ''
    else:
        patternLength = howManyDigits(mystring, lookingTo)
        return numToBinaryCompressor(patternLength) + compressHelp(mystring[patternLength:],zeroOrOne(lookingTo+1))
def howManyDigits(mystring,lookingTo):
    '''howManyDigits is a counting function that figures out how many zeros or ones exist before their respective counterpart in a string.'''
    if mystring == '':
        return 0
    elif mystring[0] == str(lookingTo):
        return 0
    else:
        return 1 + howManyDigits(mystring[1:], lookingTo)
def numToBinaryCompressor(mynumber):
    '''First tests to see if the number is greater than the max allowed length. If it is, we say that there are
    the maximum amount of digits plus the all zeros for the next digit and then finishing out that number.
    This is a helper function to be used for one number at a time. So like if the number of zeros until a 1 was
    64, then it would give out the representation for the amount of zeros.'''
    if mynumber > MAX_RUN_LENGTH:
        return '1' * COMPRESSED_BLOCK_SIZE + '0' * COMPRESSED_BLOCK_SIZE + numToBinaryCompressor(mynumber-MAX_RUN_LENGTH)
    else:
        binaryString = '0' * COMPRESSED_BLOCK_SIZE + numToBinary(mynumber)
        restrictLength = len(binaryString) - COMPRESSED_BLOCK_SIZE
        return binaryString[restrictLength:]
def zeroOrOne(mynumber):
    '''This is a check to see if the lookingTo variable stated above should be a zero or a one. If it is even, it is a zero. If it is odd, it is a one.'''
    if mynumber % 2 == 0:
        return 0
    else:
        return 1
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
def uncompress(mystring):
    '''uncompress sets up lookingTo as 0, as a counterpart for compress's looking to, which is one. Then it uses lookingTo to return
    uncompressHelp.'''
    lookingTo = 0
    return uncompressHelp(mystring,lookingTo)
def uncompressHelp(mystring,lookingTo):
    '''uncompressHelp reverses compress. It looks at the first k, or COMPRESSED_BLOCK_SIZE, numbers and converts them from binary into a number
    Then it uses that number to print out the number of either zeros or ones, whichever lookingTo is set to, as many times as it was in the original
    string. Then it adds that to the current string.'''
    if mystring == '':
        return ''
    else:
        return str(zeroOrOne(lookingTo)) * binaryToNum(mystring[0:COMPRESSED_BLOCK_SIZE]) + uncompressHelp(mystring[COMPRESSED_BLOCK_SIZE:],lookingTo+1)
def compression(mystring):
    '''Compression takes in a string of numbers and prints out the length of the numbers compressed over the original string length.'''
    return len(compress(mystring))/len(mystring)
