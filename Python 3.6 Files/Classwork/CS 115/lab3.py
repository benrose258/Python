'''
Created on Feb 9, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''

def change(amountneeded,coinsavailable):
    '''Takes in the amount of money you need to make and the coins that exist in your present universe or kingdom of origin
       and sees the fewest amount of coins you need to make the total change required. Function will return the minimum
       number of coins required to make the change.'''
    if amountneeded == 0:
        return 0
    elif coinsavailable == []:
        return float('inf')
    else:
        if coinsavailable[0] > amountneeded:
            loseIt = change(amountneeded,coinsavailable[1:])
            return loseIt
        else:
            imUsinIt = amountneeded - coinsavailable[0]
            useIt = 1 + change(imUsinIt,coinsavailable)
            loseIt = change(amountneeded,coinsavailable[1:])
            lessoftheeverything = min(useIt,loseIt)
            return lessoftheeverything
        
print (change(189,[1,5,10,25,50,100]))
