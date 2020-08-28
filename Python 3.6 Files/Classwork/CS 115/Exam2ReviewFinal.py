'''
Created on Mar 29, 2017

@author: Ben Rose
'''

def change(amountneeded,coinsavailable):
    if amountneeded == 0:
        return 0
    elif coinsavailable == []:
        return float('inf')
    elif coinsavailable[0] > amountneeded:
        loseIt = change(amountneeded,coinsavailable[1:])
        return loseIt
    else:
        useIt = 1 + change(amountneeded - coinsavailable[0], coinsavailable)
        loseIt = change(amountneeded, coinsavailable[1:])
        return min(useIt,loseIt)

def memoChange(amountneeded,coinsavailable):
    return memoChangeHelp(amountneeded,coinsavailable,{})

def memoChangeHelp(amountneeded,coinsavailable,memo):
    if (amountneeded,tuple(coinsavailable)) in memo:
        return memo[(amountneeded,tuple(coinsavailable))]
    else:
        if amountneeded == 0:
            result = 0
        elif coinsavailable == []:
            result = float('inf')
        elif coinsavailable[0] > amountneeded:
            loseIt = memoChangeHelp(amountneeded,coinsavailable[1:],memo)
            result = loseIt
        else:
            useIt = 1 + memoChangeHelp(amountneeded - coinsavailable[0], coinsavailable,memo)
            loseIt = memoChangeHelp(amountneeded, coinsavailable[1:],memo)
            result = min(useIt,loseIt)
        memo[(amountneeded,tuple(coinsavailable))] = result
        return result

def rodCutter(values,rodlength):
    if values == [] or rodlength <= 0:
        return 0
    else:
        loseIt = rodCutter(values[1:],rodlength)
        useIt = values[0][1] + rodCutter(values,rodlength - values[0][0])
        if rodlength < values[0][0]:
            return loseIt
        else:
            return max(useIt,loseIt)

def LCS(string1,string2):
    if string1 == '' or string2 == '':
        return 0
    elif string1[0] == string2[0]:
        return 1 + LCS(string1[1:],string2[1:])
    else:
        useS1 = LCS(string1[1:],string2)
        useS2 = LCS(string1,string2[1:])
        return max(useS1,useS2)

def memoLCS(string1,string2):
    return memoLCSHelp(string1,string2,{})

def memoLCSHelp(string1,string2,memo):
    if (string1,string2) in memo:
        return memo[(string1,string2)]
    else:
        if string1 == '' or string2 == '':
            result = 0
        elif string1[0] == string2[0]:
            result = 1 + memoLCSHelp(string1[1:],string2[1:],memo)
        else:
            useS1 = memoLCSHelp(string1[1:],string2,memo)
            useS2 = memoLCSHelp(string1,string2[1:],memo)
            result = max(useS1,useS2)
        memo[(string1,string2)] = result
        return result

def memoLCSWV(string1,string2):
    return memoLCSWVHelp(string1, string2, {})

def memoLCSWVHelp(string1,string2,memo):
    if (string1,string2) in memo:
        return memo[(string1,string2)]
    else:
        if string1 == '' or string2 == '':
            result = (0,'')
        elif string1[0] == string2[0]:
            loseBoth = memoLCSWVHelp(string1[1:],string2[1:],memo)
            result = (1 + loseBoth[0],string1[0] + loseBoth[1])
        else:
            useS1 = memoLCSWVHelp(string1[1:],string2,memo)
            useS2 = memoLCSWVHelp(string1,string2[1:],memo)
            result = max(useS1,useS2)
        memo[(string1,string2)] = result
        return result
