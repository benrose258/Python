#Homework 5 Redone

#Question 2

def replace(x,y,mylist):
    finallist = []
    for index in mylist:
        if index == x:
            finallist.append(y)
        else:
            finallist.append(index)
    return finallist

#Question 3

