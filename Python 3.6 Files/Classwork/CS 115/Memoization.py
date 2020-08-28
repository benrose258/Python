'''
Created on Feb 21, 2017

@author: Ben Rose
'''
#Step 1: If key is in dictionary, return value associated with key
#Step 2: Do work! Make recursive calls and store the result in a local variable
#Step 3: Store the result in the dictionary and return the result

import sys
sys.setrecursionlimit(100000)

def fib(number):
    if number <= 1:
        return number
    else:
        return fib(number - 1) + fib(number - 2)

def fibMemo(mynumber):
    def fibHelper(mynumber,dictionary):
        if mynumber in dictionary:
            return dictionary[mynumber]
        else:
            if mynumber <= 1:
                result = mynumber
            else:
                result = fibHelper(mynumber - 1,dictionary) + fibHelper(mynumber - 2,dictionary)
            dictionary[mynumber] = result
            return result
    return fibHelper(mynumber,{})

def memoLCS(string1,string2):
    def memoLCSHelp(string1,string2,memo):
        if (string1,string2) in memo:
            return memo[(string1,string2)]
        else:
            if string1 == '' or string2 == '':
                result = 0
            elif string1[0] == string2[0]:
                result = 1 + memoLCSHelp(string1[1:],string2[1:],memo)
            else:
                useS1 = memoLCSHelp(string1,string2[1:],memo)
                useS2 = memoLCSHelp(string1[1:],string2,memo)
                result = max(useS1,useS2)
            memo[(string1,string2)] = result
            return result
    return memoLCSHelp(string1,string2,{})

def memoLCSWithValues(string1,string2):
    '''Returns the length of the longest common subsequence in strings string1 and string2, as well as the string of common characters.
       The result will be a tuple.'''
    def memoLCSHelp(string1,string2,memo):
        if (string1,string2) in memo:
            return memo[(string1,string2)]
        elif string1 == '' or string2 == '':
            result = (0,'')
        elif string1[0] == string2[0]:
            #Return 1 for the counting, then plus the function, which will return a tuple, at 0, which is the value in the tuple as the first item
            #and the second item is the current string in the function plus our string at index 0.
            loseBoth = memoLCSHelp(string1[1:],string2[1:],memo)
            result =  (1 + loseBoth[0], string1[0] + loseBoth[1])
        else:
            useS1 = memoLCSHelp(string1,string2[1:],memo)
            useS2 = memoLCSHelp(string1[1:],string2,memo)
            if useS1[0] > useS2[0]:
                result = useS1
            else:
                result = useS2
        memo[(string1,string2)] = result
        return result
    return memoLCSHelp(string1,string2,{})
