#Exam 2 Review 2

def powerset(mylist):
    if mylist == []:
        return [[]]
    else:
        loseIt = powerset(mylist[1:])
        useIt = map(lambda x: [mylist[0]] + x, loseIt)
        return loseIt + useIt
