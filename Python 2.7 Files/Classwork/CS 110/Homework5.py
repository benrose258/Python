#Question 2
#Part 1
def replace(x, y, mylist):
    newlist = []
    for number in mylist:
        if number == x:
            newlist.append(y)
        else:
            newlist.append(number)
    return newlist

#Part 2
def replace(x, y, mylist):
    def helpfunc(number):
        if x == number:
            return y
        else:
            return number
    return map(helpfunc,mylist)

#Question 3
#Part 1
def x_count(x,mylist):
    howmanyx = 0
    for number in mylist:
        if number == x:
            howmanyx = howmanyx + 1
    return howmanyx

#Part 2
def add(x,y):
    return x + y
def x_count(x,mylist):
    def helpfunc(number):
        if number == x:
            return 1
        else:
            return 0
    return reduce(add,map(helpfunc,mylist))
