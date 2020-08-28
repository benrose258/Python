#Practice Exam 3 Document 3

#Question 1

def findmin(minnumber,mylist):
    if mylist == []:
        return minnumber
    elif minnumber >= mylist[0]:
        minnumber = mylist[0]
        return findmin(minnumber,mylist[1:])
    else:
        return findmin(minnumber,mylist[1:])

def minimum(mylist):
    if mylist == []:
        return "There is no minimum in the empty list."
    else:
        minnumber = mylist[0]
        return findmin(minnumber,mylist)
        
#Question 2

def succ(mynumber):
    return mynumber+1

#Question 3

def bump(mylist):
    if mylist == []:
        return []
    else:
        return [mylist[0]+1]+bump(mylist[1:])

#Question 4

def member(x,mylist):
    if mylist == []:
        return False
    elif x == mylist[0]:
        return True
    else:
        return member(x,mylist[1:])

#Question 6

def uniquify(mylist):
    if mylist == []:
        return []
    elif member(mylist[0],mylist[1:]) == False:
        return [mylist[0]]+uniquify(mylist[1:])
    else:
        return uniquify(mylist[1:])

#Question 7

def palindrome(mystring):
    if mystring == "":
        return True
    else:
        if mystring[0] == mystring[-1]:
            return palindrome(mystring[1:-1])
        else:
            return False

#Question 8

def evennumber(mynumber):
    if mynumber % 2 == 0:
        return True
    else:
        return False

def evens(mylist):
    if mylist == []:
        return []
    elif evennumber(mylist[0])==True:
        return [mylist[0]]+evens(mylist[1:])
    else:
        return evens(mylist[1:])

#Question 9

def snacks(target,mylist):
    if mylist == []:
        return 0
    elif target < mylist[0]:
        loseIt = snacks(target,mylist[1:])
        return loseIt
    else:
        useIt = 1 + snacks(target-mylist[0],mylist[1:])
        loseIt = snacks(target,mylist[1:])
        optimal = max(useIt,loseIt)
        return optimal

#Question 11

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
