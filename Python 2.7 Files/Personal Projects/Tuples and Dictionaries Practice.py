#Tuples and Memoization notes and practice

Infinity = float("inf")
D = {}

def memochange(amount,coinList):
    if amount == 0:
        return 0
    elif len(coinList) == 0:
        return Infinity
    elif (amount,coinList) in D:
        return D[(amount,coinList)]
    elif coinList[0]>amount:
        loseIt = memochange(amount,coinList[1:])
        return loseIt
    else:
        useIt = 1+memochange(amount-coinList[0],coinList)
        loseIt = memochange(amount,coinList[1:])
        optimal = min(useIt,loseIt)
        D[(amount,coinList)] = optimal
        return optimal

D2 = {}

def memoLCS(string1,string2):
    if string1 == "" or string2 == "":
        return 0
    elif (string1,string2) in D2:
        return D2[(string1,string2)]
    elif string1[0] == string2[0]:
        loseBoth = memoLCS(string1[1:],string2[1:])
        optimal = 1 + loseBoth
        D2[(string1,string2)] = optimal
        return optimal
    else:
        loseOne = memoLCS(string1[1:],string2)
        loseAnother = memoLCS(string1,string2[1:])
        optimal = max(loseOne,loseAnother)
        D2[(string1,string2)] = optimal
        return optimal

D3 = {}

def factorial(n):
    answer = 1
    for number in range(n):
        answer = answer * (n-number)
    return answer

def factorialList(mylist):
    if mylist == []:
        return []
    elif tuple(mylist) in D3:
        return D3[tuple(mylist)]
    else:
        onenumber = factorial(mylist[0])
        allnumbers = [onenumber] + factorialList(mylist[1:])
        D3[tuple(mylist)] = allnumbers
        return allnumbers

