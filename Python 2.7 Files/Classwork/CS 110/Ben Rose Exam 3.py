#Question 1(a):

def salaryUpdate(mylist):
    if mylist == []:
        return []
    else:
        return list(increase(mylist[0]))+salaryUpdate(mylist[1:])

def increase(myperson):
    modify = list(myperson)
    newmoney = [modify[0]] + [modify[1]*1.02]
    return tuple(newmoney)

#Question 2(a)

def member(checkmember,mylist):
    checkifmatch = tuple(checkmember)
    if mylist == []:
        return False
    elif checkifmatch == mylist[0]:
        return True
    else:
        return member(checkmember,mylist[1:])

def directPath(x,y,mylist):
    checkmember = tuple([x,y])
    if member(checkmember,mylist) == True:
        return True
    else:
        return False

def stepOne(x,y,mylist):
    stepOneY = "B"
    checkmember = tuple([x,stepOneY])
    if member(checkmember,mylist) == True:
        return True
    else:
        return False

def stepTwo(x,y,mylist):
    stepTwoX = "B"
    checkmember = tuple([stepTwoX,y])
    if member(checkmember,mylist) == True:
        return True
    else:
        return False

def path(x,y,mylist):
    if mylist == []:
        return False
    elif x == "D":
        return False
    elif y == "C":
        return False
    else:
        if directPath(x,y,mylist) == True:
            return True
        else:
            if stepOne(x,y,mylist) == False:
                return False
            else:
                if stepTwo(x,y,mylist) == False:
                    return False
                else:
                    return True

D = {}

def memomember(checkmember,mylist):
    if (checkmember,tuple(mylist)) in D:
        return D[(checkmember,tuple(mylist))]
    else:
        checkifmatch = tuple(checkmember)
        if mylist == []:
            D[(checkmember,tuple(mylist))] = False
            return False
        elif checkifmatch == mylist[0]:
            D[(checkmember,tuple(mylist))] = True
            return True
        else:
            return memomember(checkmember,mylist[1:])

def memodirectPath(x,y,mylist):
    checkmember = tuple([x,y])
    if memomember(checkmember,mylist) == True:
        return True
    else:
        return False

def memostepOne(x,y,mylist):
    stepOneY = "B"
    checkmember = tuple([x,stepOneY])
    if memomember(checkmember,mylist) == True:
        return True
    else:
        return False

def memostepTwo(x,y,mylist):
    stepTwoX = "B"
    checkmember = tuple([stepTwoX,y])
    if memomember(checkmember,mylist) == True:
        return True
    else:
        return False

def memopath(x,y,mylist):
    if mylist == []:
        D[(x,y,tuple(mylist))] = False
        return False
    elif (x,y,tuple(mylist)) in D:
        return D[(x,y,tuple(mylist))]
    elif x == "D":
        D[(x)] = False
        D[(x,y,tuple(mylist))] = False
        return False
    elif y == "C":
        D[(y)] = False
        D[(x,y,tuple(mylist))] = False
        return False
    else:
        if memodirectPath(x,y,mylist) == True:
            D[(x,y,tuple(mylist))] = True
            return True
        else:
            if memostepOne(x,y,mylist) == False:
                D[(x,y,tuple(mylist))] = False
                return False
            else:
                if memostepTwo(x,y,mylist) == False:
                    D[(x,y,tuple(mylist))] = False
                    return False
                else:
                    D[(x,y,tuple(mylist))] = True
                    return True

D = {}

def memosubset(target,mylist):
    if target == 0:
        return True
    elif mylist == ():
        return False
    elif (target,tuple(mylist)) in D:
        return D[(target,tuple(mylist))]
    elif target < mylist[0]:
        return memosubset(target,mylist[1:])
    else:
        useIt = memosubset(target-mylist[0],mylist[1:])
        loseIt = memosubset(target,mylist[1:])
        optimal = useIt or loseIt
        D[(target,tuple(mylist))] = optimal
        return optimal
