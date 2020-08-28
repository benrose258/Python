#Homework 3, redone for fun

#Question 1
def minlist(mylist):
    if mylist == []:
        return "There is no minimum in the empty list."
    else:
        minimum = mylist[0]
        return minlisthelp(minimum,mylist)

def minlisthelp(minimum,mylist):
    if mylist == []:
        return minimum
    else:
        if mylist[0] < minimum:
            minimum = mylist[0]
            return minlisthelp(minimum,mylist[1:])
        else:
            return minlisthelp(minimum,mylist[1:])

def minlist2(mylist):
    if mylist == []:
        return "There is no minimum in the empty list."
    else:
        minimum = mylist[0]
        for number in mylist:
            if number < minimum:
                minimum = number
        return minimum

#Question 2
def gauss(n):
    mysum = 0
    for number in range(n+1):
        mysum = mysum + number
    return mysum

#Question 3
def sumOfSquares(n):
    mysum = 0
    for number in range(n+1):
        mysum = mysum + number*number
    return mysum
