#Recursion] practice

def factorial():
    inputNum=input('input a number')
    result = 1
    for number in range(1,inputNum+1):
        result = result*number
    return result

def tothepower(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base*tothepower(base,exponent-1)

def replace(x,y,mylist):
    if mylist == []:
        return []
    else:
        if mylist[0] == x:
            return [y]+replace(x,y,mylist[1:])
        else:
            return [mylist[0]]+replace(x,y,mylist[1:])
