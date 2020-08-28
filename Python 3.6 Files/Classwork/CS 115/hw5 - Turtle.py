'''
Created on 2-27-17
@author: Ben Rose
Pledge: I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 5
'''

import turtle

'''
1. Draw tree in recursive function.
2. Call recursive function from inside another function.
3. Do turtle.done
'''

def sv_tree(trunk,levels):
    sv_tree2(trunk,levels)
    turtle.done()

def sv_tree2(trunk,levels):
    '''Using the turtle function in python, this function draws a tree. If levels == 0, this is just a straight line. If not,
    it makes a big tree using the trunk_length for the appropriate amount of levels. Running this function will literally
    show you what I mean.'''
    if levels == 0:
        return
    else:
        turtle.forward(trunk)
        turtle.left(45)
        sv_tree2(trunk/2,levels-1)
        turtle.right(90)
        sv_tree2(trunk/2,levels-1)
        turtle.left(45)
        turtle.back(trunk)

print(sv_tree(100,5))

def fast_lucas(mynumber):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fastLucasHelper(mynumber,memo):
        if (mynumber) in memo:
            return memo[(mynumber)]
        else:
            if mynumber == 0:
                result = 2
            elif mynumber == 1:
                result = 1
            else:
                result = fastLucasHelper(mynumber - 1,memo) + fastLucasHelper(mynumber-2,memo)
        memo[(mynumber)] = result
        return result
    return fastLucasHelper(mynumber,{})

def fast_change(amountneeded, coinsavailable):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amountneeded, coinsavailable, memo):
        if (amountneeded,coinsavailable) in memo:
            return memo[(amountneeded,coinsavailable)]
        else:
            if amountneeded == 0:
                result = 0
            elif coinsavailable == ():
                result = float('inf')
            elif coinsavailable[0] > amountneeded:
                loseIt = fast_change_helper(amountneeded,coinsavailable[1:],memo)
                result = loseIt
            else:
                useIt = 1 + fast_change_helper(amountneeded - coinsavailable[0],coinsavailable,memo)
                loseIt = fast_change_helper(amountneeded,coinsavailable[1:],memo)
                result = min(useIt,loseIt)
        memo[(amountneeded,coinsavailable)] = result
        return result
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amountneeded, tuple(coinsavailable), {})

print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
