'''
Created on Mar 1, 2017

@author: Ben Rose
'''

import sys
sys.setrecursionlimit(10000)

CypherIndex = { ('-1') : ( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '-', '=', '[', ']', ';', "'", ',', '.', "/", '~', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?',' '] ),
                ('0') : ( ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '-', '=', '[', ']', ';', "'", ',', '.', '/', '~', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', ' '] ),
                ('1') : ( ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z', 'a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y', 'B', 'D', 'F', 'H', 'J', 'L', 'N', 'P', 'R', 'T', 'V', 'X', 'Z', 'A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'W', 'Y', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '-', '=', '[', ']', ';', "'", ',', '.', '/', '~', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', ' '] ),
                ('2') : ( ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '-', '=', '[', ']', ';', "'", ',', '.', '/', '~', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', ' '] ),
                ('3') : ( ['t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 'l', 'a', 'z', 'y', 'd', 'g', 'T', 'H', 'E', 'Q', 'U', 'I', 'C', 'K', 'B', 'R', 'O', 'W', 'N', 'F', 'X', 'J', 'M', 'P', 'S', 'V', 'L', 'A', 'Z', 'Y', 'D', 'G', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '-', '=', '[', ']', ';', "'", ',', '.', '/', '~', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', ' '] ),
                ('4') : ( ['a', 'd', 'i', 'p', 'y', 'j', 'w', 'l', 'c', 'v', 'q', 'n', 'm', 'o', 'r', 'x', 'e', 's', 'z', 'k', 'b', 't', 'u', 'f', 'g', 'h', 'A', 'D', 'I', 'P', 'Y', 'J', 'W', 'L', 'C', 'V', 'Q', 'N', 'M', 'O', 'R', 'X', 'E', 'S', 'Z', 'K', 'B', 'T', 'U', 'F', 'G', 'H', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '-', '=', '[', ']', ';', "'", ',', '.', '/', '~', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', ' '] )
              }

original = CypherIndex['-1']

def NeoCypher():
    print ('NeoCypher 2.0')
    print()
    print('Functions:')
    print()
    print('1: File Read Mode')
    print('Enter: Default Mode')
    print()
    whichFunction = input('Please input number for function> ')
    print(clear())
    if whichFunction == '1':
        return NeoCypherFileRead()
    elif whichFunction == '':
        print('Selected: Default Mode')
        print()
        mymessage = input('Please enter message> ')
        print ()
        print ('Press enter when finished with code entry.')
        print ()
        codeList = NeoCypherNumber([])
        return NeoCypherBrain([mymessage], codeList, 0)
    else:
        print('Error: Please enter a corresponding function number or press enter.')
        print()
        return NeoCypher()

def NeoCypherFileRead():
    print('Selected: File Read Mode')
    data = []
    fileRead = input('File Name: ')
    fileCypher = open(fileRead)
    for index in fileCypher:
        data.append(index.strip())
    fileCypher.close
    codeList = NeoCypherNumber([])
    return NeoCypherBrain(data,codeList,0)

def NeoCypherNumber(codeList):
    cyphernumber = input('Please enter code> ')
    if cyphernumber == '':
        return codeList
    else:
        if len(cyphernumber) > 1:
            print('Error: Please put in a number 0-9.')
            print()
            return NeoCypherNumber(codeList)
        else:
            codeList = codeList + [cyphernumber]
            return NeoCypherNumber(codeList)

def NeoCypherBrain(fileData,codeList,counter):
    if codeList == [] and fileData == []:
        return ''
    elif codeList == []:
        print (fileData[0])
        return NeoCypherBrain(fileData[1:],codeList,counter)
    else:
        if counter >= len(fileData):
            return NeoCypherBrain(fileData,codeList[1:],0)
        else:
            if counter == 0:
                fileData = [NeoCypherBrainHelper(fileData[counter],codeList[0])] + fileData[counter+1:]
                return NeoCypherBrain(fileData, codeList, counter+1)
            else:
                fileData = fileData[:counter] + [NeoCypherBrainHelper(fileData[counter],codeList[0])] + fileData[counter+1:]
                return NeoCypherBrain(fileData, codeList, counter+1)

def NeoCypherBrainHelper(mymessage,cyphernumber):
    '''Takes in a message and the number value corresponding to the cypher
       that will be used. Outputs the encoded value going from the original
       list of alphanumerical characters to the cyphered character. The
       cyphernumber will be a string and will correspond to a cypher in the
       CypherIndex dictionary.'''
    if mymessage == '':
        return ''
    else:
        if cyphernumber in CypherIndex:
            currentCypher = CypherIndex[cyphernumber]
            return currentCypher[locationChecker(mymessage[0],original)] + NeoCypherBrainHelper(mymessage[1:],cyphernumber)
        elif int(cyphernumber) in range(5,10):
            currentCypher = CypherIndex[str(int(cyphernumber)-5)]
            return original[locationChecker(mymessage[0], currentCypher)] + NeoCypherBrainHelper(mymessage[1:],cyphernumber)
        else:
            print('Error: Please put in a number 0-9.')
            print('')
            return mymessage

def locationChecker(myletter,myCypher):
    '''Returns the index of the letter in the myCypher list'''
    for index in range(len(myCypher)):
        if myletter == myCypher[index]:
            return index

def clear():
    mylist = [''] * 50
    for index in mylist[:-1]:
        print()
    return mylist[-1]

print(NeoCypher())

#Order: lowercase letters, uppercase letters, numbers, shift-numbers,symbols,shift-symbols
