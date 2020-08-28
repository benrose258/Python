def odd(x):
    if x % 2 != 0:
        return True
    else:
        return False

def helperfunc(mylist):
    finallist == []
    for index in mylist:
        if mylist[odd(index)] == True:
            finallist.append(index)
    return finallist

def logicfunction(n):
    mylist = range(1,n)
    value1 = sum(helperfunc(mylist))
    value2 = n**2
    print (value1)
    print (value2)
    if value1 == value2:
        return True
    else:
        return False
