#Homework 4, redone for fun

#Question 1

def head(mylist):
    if mylist == []:
        return "Error: the empty list has no head."
    else:
        return mylist[0]

#Question 2

def tail(mylist):
    if mylist == []:
        return "Error: the empty list has no tail."
    else:
        return mylist[1:]

#Question 3

def replace_and_triple(x,y,z,mylist):
    if mylist == []:
        return mylist
    else:
        finallist = []
        for index in mylist:
            if index == x:
                finallist.append(y)
            elif index == z:
                finallist.append(3*z)
            else:
                finallist.append(index)
        return finallist
