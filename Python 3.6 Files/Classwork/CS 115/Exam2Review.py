'''
Created on Mar 28, 2017

@author: Ben Rose
'''

def LCS(string1,string2):
    if string1 == '' or string2 == '':
        return 0
    elif string1[0] == string2[0]:
        return 1 + LCS(string1[1:],string2[1:])
    else:
        useS1 = LCS(string1[1:],string2)
        useS2 = LCS(string1, string2[1:])
        return max(useS1,useS2)

def memoLCS(string1,string2):
    return memoLCSHelper(string1,string2,{})

def memoLCSHelper(string1,string2,memo):
    if (string1,string2) in memo:
        return memo[(string1,string2)]
    else:
        if string1 == '' or string2 == '':
            result = 0
        elif string1[0] == string2[0]:
            result = 1 + memoLCSHelper(string1[1:],string2[1:],memo)
        else:
            useS1 = memoLCSHelper(string1[1:], string2, memo)
            useS2 = memoLCSHelper(string1,string2[1:],memo)
            result = max(useS1,useS2)
    memo[(string1,string2)] = result
    return result

def ED(string1,string2):
    if string1 == '':
        return len(string2)
    elif string2 == '':
        return len(string1)
    else:
        if string1[0] == string2[0]:
            return ED(string1[1:],string2[1:])
        else:
            substitution = 1 + ED(string1[1:],string2[1:])
            useS1 = 1 + ED(string1[1:],string2)
            useS2 = 1 + ED(string1,string2[1:])
            return min(substitution,useS1,useS2)

def memoED(string1,string2):
    return memoEDHelper(string1,string2,{})

def memoEDHelper(string1,string2,memo):
    if (string1,string2) in memo:
        return memo[(string1,string2)]
    else:
        if string1 == '':
            result = len(string2)
        elif string2 == '':
            result = len(string1)
        else:
            if string1[0] == string2[0]:
                result = memoEDHelper(string1[1:],string2[1:],memo)
            else:
                substitution = 1 + memoEDHelper(string1[1:], string2[1:], memo)
                useS1 = 1 + memoEDHelper(string1[1:],string2,memo)
                useS2 = 1 + memoEDHelper(string1, string2[1:], memo)
                result = min(substitution,useS1,useS2)
        memo[(string1,string2)] = result
        return result

def memoLCSWithValues(string1,string2):
    return memoLCSWithValuesHelper(string1,string2,{})

def memoLCSWithValuesHelper(string1,string2,memo):
    if (string1,string2) in memo:
        return memo[(string1,string2)]
    else:
        if string1 == '' or string2 == '':
            result = (0,'')
        elif string1[0] == string2[0]:
            loseBoth = memoLCSWithValuesHelper(string1[1:], string2[1:], memo)
            result = (1 + loseBoth[0],string1[0] + loseBoth[1])
        else:
            useS1 = memoLCSWithValuesHelper(string1[1:], string2, memo)
            useS2 = memoLCSWithValuesHelper(string1, string2[1:], memo)
            result = max(useS1,useS2)
    memo[(string1,string2)] = result
    return result

def rodCutter(values,mynumber):
    if values == [] or mynumber <= 0:
        return 0
    else:
        loseIt = rodCutter(values[1:],mynumber)
        useIt = values[0][1] + rodCutter(values,mynumber - values[0][0])
        if values[0][0] > mynumber:
            return loseIt
        else:
            return max(useIt,loseIt)
