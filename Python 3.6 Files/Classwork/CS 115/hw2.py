'''
Created on Feb 6, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''

#from dict import Dictionary
from bigdict import Dictionary
import sys
from cs115 import map,reduce,filter
sys.setrecursionlimit(10000)

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1],
["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1],
["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1],
["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

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

def counter(myletters,mycounter,mytestingletters,myletter):
    '''counter takes in a static list of usable letters, a counter, a dynamic list of usable letters (equivalent to myletters upon the
       first function call), and one single letter that is currently being tested against our list of usable letters. The overall purpose
       of this function is to tell the rest of the program that when you are using a letter in your total list of letters, the letter is
       no longer available to be used for the rest of the word. The first if statement is error checking if we have very specific conditions:
       if our list of possible letters to test consists of just one letter, we have not tested any letters (meaning that our list had one
       and only one letter since the function ran) and the letter is equal to the character in the list of possible letters, then just return
       that letter/word. This is covering the only two possible and necessary cases where this error handling is neccessary: if the word is
       "i" or the word is "a" and we only had "i" or "a" in the possible numbers we could use. If it is, it is the only time this function
       will return a letter instead of a numerical value. Otherwise, the program will run through the list of letters provided until it finds
       the correct letter. The reason we don't have a base case where the letter is not in our possible letters is in the function this
       function will be applied, counter will only be run if we detect that a letter in our provided letters is equal to a letter in the word.
       If not, there is no reason to make a revised version of our total remaining letters as it will remain the same. This function will
       return our new list of remaining letters without the letter we just used.'''
    if len(mytestingletters) == 1 and mytestingletters[0] == myletter and mycounter == 0:
        return myletters[:-1]
    elif mytestingletters[0] == myletter:
        return myletters[0:mycounter] + mytestingletters[1:]
    else:
        mycounter = mycounter + 1
        return counter(myletters,mycounter,mytestingletters[1:],myletter)

def member(myletters, myword, mychangingletters):
    '''member takes in our static list of provided available letters, a word, and a list of dynamic available letters (which will be equal
       to our static list of letters at the beginning of our original call of the function) and will return whether it is possible to make
       our provided word with the letters we have available. The output will be either True or False. In regard to the base cases: for the
       first base case, if our list of possible letters does not contain a letter in our word, then the word cannot be made, and hence the
       function will return False. If we have run out of letters in our word to test (if every letter in the word can be used), then we can
       make this word, and our function will return True. However if we have not tested every letter in the word and haven't come up empty
       yet, we will move to the else statement. First we have a counter, which will be used in our counter function listed above, which will
       begin at 0 for every time we are checking a letter. Then we will define our variable mytestingletters, which will be used as the
       dynamic list of letters in the counter function. If we were to use our existing mychangingletters list in place for the member
       function, however, we may not be able to test all of the letters in our list of letters. This is because, if the first index
       in mychangingletters is not equal to the first letter in myword, then we will remove it for the remainder of the test for that letter.
       So in short we would be unable to return the correctly modified list from counter if we used an incomplete list to begin with.
       If we are able to use a letter, going back to this function, then we call the function once more, testing every letter in our
       list of remaining letters against all of the letters we have not yet tested in the word. If we are not able to use the letter, however,
       we will keep checking the dynamic list against the letter in the word from the dynamic list from the first character onward.
       And again we will output True or False based on the results.'''
    if mychangingletters == []:
        return False
    elif myword == '':
        return True
    else:
        mycounter = 0
        mytestingletters = myletters
        if mychangingletters[0] == myword[0] and myword[0] == myword:
            return True
        elif mychangingletters[0] == myword[0]:
            mychangingletters = counter(myletters,mycounter,mytestingletters,mychangingletters[0])
            return member(myletters,myword[1:],mychangingletters)
        else:
            return member(myletters,myword,mychangingletters[1:])

def scoreList(myletters):
    '''scoreList in itself is really a gateway function. Because we are required to only have one input (our available letters), this
       function is used to set up a supplementary function which will do the work for this function's output. This function, when called
       itself, will return the results of the supplementary function with the original function's created variables, which will be a list
       of all possible words that can be made with our provided dictionary of words (given in the function's code), and creates the dynamic
       list mychangingletters from the static list myletters that was input at the start of the function.'''
    dictionarywords = Dictionary
    mychangingletters = myletters
    return scoreListBrain(myletters,dictionarywords,mychangingletters)

def scoreListBrain(myletters,dictionarywords,mychangingletters):
    '''scoreListBrain is the supplementary function for scoreList, taking in the words in our given dictionary, our static list of letters,
       and our dynamic list of letters, and returns a list of all possible words that can be made in our Dictionary with the letters provided.
       The base case is when we have no more words in our Dictionary to test, which will return an empty list to add to our list of possible
       words. Otherwise, we will create a variable testword for the current word in the dictionary we are testing. If the output of the member
       function, given the inputs myletters, mychangingletters, and the word we are testing, returns True, then we will take that word and
       check its total numerical score using our wordScore function previously defined, given the word and the values of the letters. If
       member returns False, however, then we will just move on to the next word in the dictionary and not add anything to our list of
       possible words. This function, as stated above, will return a list containing all the possible words in the provided dictionary that
       are possible to be made with our available letters and their respective values.'''
    if dictionarywords == []:
        return []
    else:
        testword = dictionarywords[0]
        if member(myletters,testword,mychangingletters) == True:
            return [[testword] + [wordScore(testword,scrabbleScores)]]+scoreListBrain(myletters,dictionarywords[1:],mychangingletters)
        else:
            return scoreListBrain(myletters,dictionarywords[1:],mychangingletters)

def bestWord(myletters):
    '''This function, like scoreList, is more of a setup for its supplementary function using the available variables. It will return
       the result of the subsequent function using a variable mypossiblebest, which is a list of the words and values provided by scoreList
       given our available letters. The final result of this function will be the word with the highest value out of our list of possible
       words.'''
    mypossiblebest = scoreList(myletters)
    return bestWordBrain(mypossiblebest)

def bestWordBrain(mypossiblebest):
    '''This function will return the word that will give you the greatest possible points out of the list of possible words. First, if there
       are no items in the list of possible words, we will return an empty string followed by the value 0, as we don't have a word, and no
       word returns the value 0, as nothing doesn't have a value. If the list is not empty, however, we will first create a word to check
       against, which will be our first word in our list of possible words. This variable, named firstpossiblebest, will be checked against
       the rest of the values in the entire list of mypossiblebest by comparing firstpossiblebest[1] against the next possible best at [1],
       comparing the values of the two words. If the value of the next possible best is greater than the value of the current best, then
       the current best will be replaced, and the function will continue until we have only one word remaining, which will be the word with
       the highest possible value. Then the function, as stated above, will return this word with its numerical value.'''
    if mypossiblebest == []:
        return ['',0]
    firstpossiblebest = mypossiblebest[0]
    otherpossiblebest = bestWordBrain(mypossiblebest[1:])
    if firstpossiblebest[1] > otherpossiblebest[1]:
        return firstpossiblebest
    else:
        return otherpossiblebest

print(scoreList(['t','e','l','h','n','i','m']))
