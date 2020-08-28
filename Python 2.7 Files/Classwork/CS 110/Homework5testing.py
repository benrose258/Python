def replace(x, y, mylist):
    newlist = ""
    for letter in mylist:
        if letter == x:
            newlist = newlist + y
        else:
            newlist = newlist + letter
    return newlist

def minfunc(mylist):
    minNumber = mylist[0]
    for number in mylist:
        if number >= minNumber:
            pass
        else:
            minNumber = number
    return minNumber
