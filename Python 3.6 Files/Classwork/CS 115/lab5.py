'''
Created on: 2-24-17
@author: Ben Rose
Pledge: I pledge my honor that I have abided by the stevens honor system. -Ben Rose

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10

def fastED(string1, string2):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fastEDHelp(string1,string2,memo):
        if (string1,string2) in memo:
            return memo[(string1,string2)]
        elif string1 == '':
            result = len(string2)
        elif string2 == '':
            result = len(string1)
        elif string1[0] == string2[0]:
            result = fastEDHelp(string1[1:],string2[1:],memo)
        else:
            useS1 = 1 + fastEDHelp(string1,string2[1:],memo)
            useS2 = 1 + fastEDHelp(string1[1:],string2,memo)
            loseBoth = 1 + fastEDHelp(string1[1:],string2[1:],memo)
            result = min(useS1,useS2,loseBoth)
        memo[(string1,string2)] = result
        return result
    return fastEDHelp(string1,string2,{})

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda word: (fastED(user_input,word),word),words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
