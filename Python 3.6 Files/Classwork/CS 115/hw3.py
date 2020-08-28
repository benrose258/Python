'''
Created on Feb 9, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function givegiveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amountneeded,coinsavailable):
    '''Takes in the amount of money you need to make and the coins that exist in your present universe or kingdom of origin
       and sees the fewest amount of coins you need to make the total giveChange required. Function will return the minimum
       number of coins required to make the giveChange and the coins you need to use.'''
    if amountneeded == 0:
        return [0,[]]
    elif coinsavailable == []:
        return [float('inf'),[]]
    else:
        if coinsavailable[0] > amountneeded:
            return giveChange(amountneeded,coinsavailable[1:])
        else:
            useIt = giveChange(amountneeded - coinsavailable[0],coinsavailable)
            loseIt = giveChange(amountneeded,coinsavailable[1:]) 
            if loseIt[0] < 1 + useIt[0]:
                return loseIt
            else:
                return [1 + useIt[0],[coinsavailable[0]] + useIt[1]]

print(giveChange(13,[1,2,5,10]))

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def wordsWithScore(dictionary,scorelist):
    '''Returns a list of words in dictionary with their Scrabble score.'''
    dictionarywords = dictionary
    return scoreListBrain(dictionarywords)

def wordsWithScoreBrain(dictionarywords):
    '''Takes in a list of dictionary words and returns the value and word for each word using the helper function wordScore.'''
    if dictionarywords == []:
        return []
    else:
        myword = dictionarywords[0]
        return [[myword] + [wordScore(myword,scrabbleScores)]]+wordsWithScoreBrain(dictionarywords[1:])
    
def letterScore(letter,scorelist):
    '''letterScore takes in a single letter and a list of all letters with their corresponding numerical values.
       letterScore then checks the provided letter against the first item in the scorelist. If the letter is not
       equal to the letter in the first index in the first item in scorelist (ex of first item in scorelist: ['a',1])
       (then that first item is now separate from our larger scorelist, and then the first index of our sublist, ['a',1],
       which we can dub checkletter, is checked against our variable "letter"). If letter is not equal to checkletter[0],
       the function moves on to the remaining characters in scorelist until it finds a match. A case where our scorelist
       is unneccesary in this case as long as we have defined numerical values for every letter in the alphabet and our
       input "letter" is in the same case (capitalization-wise). This function returns the numerical value for the given letter.'''
    checkletter = scorelist[0]
    if letter == checkletter[0]:
        return checkletter[1]
    else:
        return letterScore(letter,scorelist[1:])

def wordScore(myword,scorelist):
    '''wordScore takes in a word and a scorelist that contains the numerical value of letters. wordScore uses recursion and letterScore
       to check the value first of every character in the word and adding them together. The base case is zero because if we do not have
       any letter to check, there will be no value associated with that call. This function will return the numerical score of a word.'''
    if myword == '':
        return 0
    else:
        return letterScore(myword[0],scorelist) + wordScore(myword[1:],scorelist)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(mynumber,mylist):
    '''Returns the list mylist[0:mynumber].'''
    finallist = []
    counter = 0
    return takeBrain(mylist, mynumber, counter, finallist)

def takeBrain(mylist,mynumber,counter,finallist):
    '''Takes a number mynumber, a list mylist, a counter beginning at 0, and an empty list. As long as the counter has not reached the number, we will
       keep adding every index of my list until our list is of length 8. This will return mylist[0:mynumber].'''
    if mylist == []:
        return []
    else:
        if counter < mynumber:
            finallist = finallist + [mylist[0]]
            counter = counter + 1
            return takeBrain(mylist[1:],mynumber,counter,finallist)
        else:
            return finallist



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(mynumber, mylist):
    '''Returns the list mylist[mynumber:].'''
    counter = 0
    return dropBrain(mynumber,mylist,counter)  # your code goes here

def dropBrain(mynumber,mylist,counter):
    '''Takes the number mynumber, a list of numbers, and a counter initially equal to 0. Until the counter is equal to the number, we will lose the
       first element of mylist. This will return mylist[mynumber:].'''
    if mylist == []:
        return []
    else:
        if counter < mynumber:
            mylist = mylist[1:]
            counter = counter + 1
            return dropBrain(mynumber,mylist,counter)
        else:
            return mylist
