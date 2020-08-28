'''
Created on Feb 13, 2017

@author: Ben Rose
'''

def identifyletter(myletter, mystring):
    if mystring == '':
        return False
    elif myletter == mystring[0]:
        return True
    else:
        return identifyletter(myletter,mystring[1:])

def identifysequence(mysequence,mystring):
    if mysequence == '':
        return True
    elif mystring == '':
        return False
    else:
        if identifyletter(mysequence[0],mystring) == False:
            return identifysequence(mysequence,mystring[1:])
        else:
            return identifysequence(mysequence[1:],mystring[1:])

def countersequence(mysequence,mystring,counter,wordcounter):
    if mysequence == '':
        return counter
    elif mystring == '':
        return -1
    else:
        if identifyletter(mysequence[0],mystring[0]) == False:
            counter = counter+1
            return countersequence(mysequence,mystring[1:],counter)
        else:
            counter = counter+1
            wordcounter = wordcounter+1
            if wordcounter < counter:
                '''If wordcounter hasn't increased at the same rate as counter (i.e. the letters are not consecutive),
                   then add the regular counter plus the difference between counter and wordcounter.'''
                counter = counter + counter - wordcounter
                return countersequence(mysequence[1:],mystring[1:],counter)

def identifyArea(startingsequence,endingsequence,mystring):
    '''This program will identify and print code beginning with a specified starting sequence and an ending sequence and print out
       that specific line. Works for strings only.'''
    if mystring == '':
        return 'ERROR: NO STRING'
    elif startingsequence == '':
        return 'ERROR: NO STARTING SEQUENCE'
    elif endingsequence == '':
        return 'ERROR: NO ENDING SEQUENCE'
    elif len(mystring) < len(startingsequence):
        return 'ERROR: STARTING SEQUENCE NOT IN STRING'
    else:
        startlength = len(startingsequence)
        if mystring[0:startlength] == startingsequence:
            print ('STARTING SEQUENCE IDENTIFIED')
            endstring = mystring[startlength:]
            if identifyEndingArea(endingsequence, endstring) == float('inf'):
                return 'ERROR: ENDING SEQUENCE NOT IN STRING'
            else:
                return startingsequence[:-1] + '("' + endstring[0:identifyEndingArea(endingsequence,endstring)] + endingsequence + ')'
            '''return startingsequence + endstring[0:identifyEndingArea(endingsequence,endstring)] + endingsequence'''
        else:
            return identifyArea(startingsequence,endingsequence,mystring[1:])

def identifyEndingArea(endingsequence,endstring):
    if len(endingsequence) > len(endstring):
        return float('inf')
    elif endingsequence == endstring[0:len(endingsequence)]:
        return 0
