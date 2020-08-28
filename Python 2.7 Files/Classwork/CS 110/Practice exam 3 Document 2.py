#Practice exam 3 second review

#Question 3

def bump(mylist):
    if mylist == []:
        return []
    else:
        return [mylist[0]+1]+bump(mylist[1:])

#Question 8

def evens(mylist):
    if mylist == []:
        return []
    else:
        if mylist[0]%2 == 0:
            return [mylist[0]]+evens(mylist[1:])
        else:
            return evens(mylist[1:])

#Question 2

def succ(mynumber):
    mynumber = mynumber+1
    return mynumber

#Question 1

def minimum(mylist):
    if mylist == []:
        return "There is no minimum in the empty list."
    else:
        finalnumber = mylist[0]
        return helpfindmin(finalnumber,mylist)

def helpfindmin(finalnumber,mylist):
    if mylist == []:
        return finalnumber
    else:
        if finalnumber>=mylist[0]:
            finalnumber = mylist[0]
            return helpfindmin(finalnumber,mylist[1:])
        else:
            return helpfindmin(finalnumber,mylist[1:])

#Question 4

def member(x,mylist):
    if mylist == []:
        return False
    else:
        answer = False
        return checkformember(x,answer,mylist)

def checkformember(x,answer,mylist):
    if answer == True:
        return True
    if mylist == [] and answer == False:
        return False
    else:
        if mylist[0]==x:
            answer = True
            return checkformember(x,answer,mylist)
        else:
            return checkformember(x,answer,mylist[1:])

#Question 6

def uniquify(mylist):
    if mylist == []:
        return mylist
    else:
        if member(mylist[0],mylist[1:]) == True:
            return uniquify(mylist[1:])
        else:
            return [mylist[0]]+uniquify(mylist[1:])

#Question 7

def palindrome(mystring):
    if mystring == "":
        return True
    else:
        if mystring[0] == mystring[-1]:
            return palindrome(mystring[1:-1])
        else:
            return False

#Question 9

def snacks(target,mylist):
    if mylist == []:
        return target
    elif target == 0:
        return 0
    elif mylist[0]>target:
        return snacks(target,mylist[1:])
    else:
        useIt = snacks((target-mylist[0]),mylist[1:])
        loseIt = snacks(target,mylist[1:])
        return useIt or loseIt

#Question 11

D = {}
def memosubset(target,mylist):
    if target == 0:
        return True
    elif mylist == []:
        return False
    elif (target,tuple(mylist)) in D:
        return D[(target,tuple(mylist))]
    else:
        useIt = memosubset(target-mylist[0],mylist[1:])
        loseIt = memosubset(target,mylist[1:])
        optimal = useIt or loseIt
        D[(target,tuple(mylist))] = optimal
        return optimal
