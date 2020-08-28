'''
Created on Apr 10, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''

DATABASE = "musicrecplus.txt"

def readUserPreferences(filename):
    '''Reads user preferences from a file.'''
    dataFile = open(filename, 'r')   # Open the file for reading.
    userData = {}
    for line in dataFile:            # Get one line at a time.
        [user, artists] = line.strip().split(':')
        artists = artists.split(',')
        artists.sort()
        user = user.strip()
        userData[user] = artists,len(artists)
    dataFile.close() # Important - do not forget to close the file
    return userData

userData = readUserPreferences(DATABASE)

def saveUserPreferences(filename):
    '''Saves preferences to a file.'''
    dataFile = open(filename,'w')
    for user in userData:
        userString = ''
        for artist in userData[user][0]:
            if artist == userData[user][0][-1]:
                userString += artist
            else:
                userString += artist + ','
        saveData = str(user) + ':' + userString + '\n'
        dataFile.write(saveData)
    dataFile.close()
    
def optOutCheck(name):
    '''Checks if a user has opt-out enabled.'''
    if name[-1] == '$':
        return 'Error'
    else:
        if userData[name + '$'][0][0] == 'Y':
            return 'on'
        elif userData[name + '$'][0][0] == 'N':
            return 'off'

def enterPref(name):
    '''Serves as a menu for all preference choices as well as making the initial preferences for new users.'''
    if name in userData:
        # Insert delete preference, or toggle opt-out
        print('Which preference option would you like to use?')
        print('1. Toggle opt-out')
        print('2. Add new liked artists')
        print('3. Delete existing liked artists')
        print('4. View all settings')
        print()
        whichPreference = input('Please input a option number> ')
        print()
        return prefChoice(name,whichPreference)
    else:
        print('Welcome',name + '! Since you are a new user, I will need to gather some info about your music preferences.')
        print()
        artists = prefEntry()
        if artists == []:
            resultData = ([''],0)
        else:
            howManyLikes = len(artists)
            resultData = (artists,howManyLikes)
        userData[(name)] = resultData
        return resultData

def prefChoice(name,whichPreference):
    '''Contains all of the preference options: toggle opt-out, enter new artists, delete artists, and show all preferences.'''
    if whichPreference == '1':
        '''Allows user to switch their opt-out preferences.'''
        print('Currently, opt-out is ' + optOutCheck(name) + '. To change this, press any key. To leave it as is, just press enter.')
        change = input('Please enter any key to toggle or press enter to exit> ')
        print()
        if change != '':
            if optOutCheck(name) == 'on':
                toggle = 'N'
            else:
                toggle = 'Y'
            userData[(str(name + '$'))] = ([toggle],1)
            print('Your settings have been changed to ' + optOutCheck(name) + '. Thank you.')
            return ''
        else:
            print( 'Your settings have been left as-is. Thank you.')
            return ''
    elif whichPreference == '2' or whichPreference == '3' or whichPreference == '4':
        artistCounter = 1
        print('Your current music preferences include:')
        for artist in userData[name][0]:
            print(str(artistCounter) + '. ' + artist)
            artistCounter += 1
        print()
        if whichPreference == '2':
            '''Allows user to enter new artists.'''
            newData = prefEntry()
            if newData != []:
                moreLikes = len(newData)
                newArtistList = userData[name][0] + newData
                newArtistList.sort()
                newResult = (newArtistList,userData[name][1] + moreLikes)
                userData[(name)] = newResult
        elif whichPreference == '3':
            '''Allows user to delete old artists.'''
            print('Please input a number from the above list to remove from your list or press enter to exit.')
            artistNum = input('Please input a number or enter to exit> ')
            if artistNum == '':
                return ''
            else:
                artistNum = int(artistNum)
                myPrefs = list(userData[name][0])
                if artistNum > len(myPrefs):
                    print('Error: Artist number not found. Please try again.')
                    return prefChoice(name,'3')
                elif artistNum == len(myPrefs):
                    newPrefs = myPrefs[:artistNum - 1]
                else:
                    newPrefs = myPrefs[:artistNum-1] + myPrefs[artistNum:]
                userData[name] = (newPrefs,userData[name][1]-1)
                print('Your preferences have been changed. Thank you.')
                print()
                return prefChoice(name, '3')
        elif whichPreference == '4':
            '''Prints all of the user's preferences. The music preferences were printed above (see above option 2)'''
            print ('Opt-Out: ' + optOutCheck(name))
            return ''
        else:
            print('Error: function not listed. Please try again.')
            return ''

def prefEntry():
    '''Helper function, returns a list of entered preferences from the user.'''
    artists = []
    enterArtist = None
    while enterArtist != '':
        enterArtist = input('Enter an artist you like or press enter to exit> ')
        if enterArtist == '':
            break
        else:
            artists.append(enterArtist)
    return artists

def getRecommendations(name):
    '''If there is only one user or all other users have opt-out on, this function returns an error. Otherwise, it gets
    the user with the closest preferences to the active user and returns artists that they do not share.'''
    bestUser = findBestUser(name)
    if bestUser == None:
        print('''Error: No other user preferences available to scan.
This could be because all other users are set to opt-out mode or no other users are registered.
Sorry for the inconvenience.'''
              )
        return ''
    else:
        recommended = drop(userData[name][0],userData[bestUser][0])
        print('Here are some artists I think you might like:')
        for index in range(len(recommended) + 1):
            if index == len(recommended):
                return ''
            else:
                print(recommended[index])

def findBestUser(name):
    '''Finds the user that has the closest preferences to the user who called the function out of all users that
    do not have opt-out enabled.'''
    mypreferences = userData[name][0]
    bestUser = None
    bestScore = -1
    for user in userData:
        if optOutCheck(user) == 'off':
            score = numMatches(mypreferences,userData[user][0])
            if score > bestScore and user != name:
                bestScore = score
                bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    finallist = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            finallist.append(list2[j])
            j += 1
    
    return finallist

def numMatches(list1, list2):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def mostLikes():
    '''Using every user who has opt-out off, this function finds out which user has the most likes and returns their name.'''
    topLikesUser = [('',0)]
    for user in userData:
        if optOutCheck(user) == 'off':
            if topLikesUser[0][1] < userData[user][1]:
                topLikesUser = [(str(user),userData[user][1])]
            elif topLikesUser[0][1] == userData[user][1]:
                topLikesUser += [(str(user),userData[user][1])]
    if len(topLikesUser) == 1:
        print('Currently, the user with the most likes is ' + topLikesUser[0][0] + ', with ' + str(topLikesUser[0][1]) + ' like(s)!')
    elif len(topLikesUser) == 2:
        print('Currently, the users with the most likes are ' + str(topLikesUser[0][0]) + ' and ' + str(topLikesUser[1][0]) + ', both with ' + str(topLikesUser[0][1]) + ' like(s)!')
    else:
        topUsers = ''
        for user in topLikesUser:
            if user == topLikesUser[-1][0]:
                topUsers += 'and' + user
            else:
                topUsers += user + ', '
        print('Currently, the users with the most likes are ' + topUsers + ' with ' + str(topLikesUser[0][1]) + ' likes each!')
    return ''

def mostPopularArtist():
    '''Creates an artistList of all of the artists that users without opt-out enabled like. Then gets the best artist data
    from its helper function and returns the best artist.'''
    artistList = []
    for user in userData:
        if optOutCheck(user) == 'off':
            artistList += userData[user][0]
    artistList.sort()
    bestArtist = findBestArtist(artistList)
    if len(bestArtist[0]) == 1:
        return 'The most popular artist is \'' + bestArtist[0][0] + '\' with ' + str(bestArtist[1]) + ' like(s)!'
    else:
        print ('The most popular artists are:')
        for index in bestArtist[0]:
            print(index)
        return 'with ' + str(bestArtist[1]) + ' like(s) each!'

def findBestArtist(artistList):
    '''Using the artistList created in mostPopularArtist, this function searches through the list and pulls out the artist or artists
    that have the most likes. Because the list has been sorted alphabetically, the function is able to detect this by counting
    how many times an artist appears until the next artist.'''
    bestArtist = ([],0)
    counter = 1
    currentArtist = artistList[0]
    indexnum = 0
    while indexnum < len(artistList) - 1:
        if artistList[indexnum + 1] == currentArtist:
            counter += 1
        else:
            if bestArtist[1] < counter:
                bestArtist = ([currentArtist],counter)
                counter = 1
                currentArtist = artistList[indexnum+1]
            elif bestArtist[1] == counter:
                bestArtist = (bestArtist[0] + [currentArtist],counter)
                counter = 1
                currentArtist = artistList[indexnum+1]
            else:
                counter = 1
                currentArtist = artistList[indexnum + 1]
        indexnum += 1
    if bestArtist[1] < counter:
        bestArtist = ([currentArtist],counter)
    elif bestArtist[1] == counter:
        bestArtist = (bestArtist[0] + [currentArtist],counter)
    return bestArtist

def firstTimePrompt():
    '''Provides an initial prompt for the user. If the user exists, move right to the regular prompt. If not, first get
    their preference data on opt-out and store either a 'Y' or 'N' in name + $, where name is the user's name. Then move
    the user to put in their initial preferences.'''
    print('Welcome to Music Recommender 2.0!')
    print()
    name = input('Please enter your name> ')
    print()
    if name in userData:
        print('Welcome back',name+'!')
        return prompt(name)
    else:
        print('''Since you\'re new here, I would like to explain our opt-out feature. If you wish, you can add a $ to the end of
your name and your name and preferences will not be displayed to other users. This will exclude your preferences from
general statistics such as finding the most popular artists, the user with the most likes, and recommendations for other
users. If you feel you reached this page in error, then input a * into the prompt below.
If you would like to enable opt-out mode, input a $ into the prompt below. Otherwise, just press the enter key.
This feature can be changed later.''')
        print()
        optOut = input('Please enter *, $, or press enter> ')
        print()
        if optOut == '*':
            return firstTimePrompt()
        elif optOut == '$':
            userData[(name+'$')] = 'Y'
        else:
            userData[(name+'$')] = 'N'
        enterPref(name)
        return prompt(name)

def continueToPrompt(name):
    '''A function to improve the UI. Instead of going directly to the prompt, the user is able to view the data from their
    previous function and then move on when ready instead of scrolling back up.'''
    print()
    continueNow = input('Press enter to continue... ')
    return prompt(name)
    
def prompt(name):
    '''Main prompt, contains all options that the program can use.'''
    print()
    print('''Enter a letter to choose an option:
        x - Manage all preferences
        t - Toggle Opt-Out status
        e - Enter music preferences
        d - Delete music preferences
        s - Show all preferences
        r - Get recommendations
        p - Show most popular artists and the artist's likes
        m - Which user has the most likes
        q - Save and quit''')
    print()
    getInput = input('Please enter letter> ')
    print()
    if getInput == 'x':
        enterPref(name)
        #Go to general preference management
    elif getInput == 't':
        prefChoice(name, '1')
        #Go to toggle Opt-out function
    elif getInput == 'e':
        prefChoice(name,'2')
        #Go to enter preferences function
    elif getInput == 'd':
        prefChoice(name,'3')
        #Go to delete preferences function
    elif getInput == 's':
        prefChoice(name,'4')
        #Go to show preferences function
    elif getInput == 'r':
        getRecommendations(name)
        #Go to recommendations function
    elif getInput == 'p':
        print(mostPopularArtist())
        #Go to Most Popular Artists Function
    elif getInput == 'm':
        print(mostLikes())
        #Go to Top User Likes function
    elif getInput == 'q':
        saveUserPreferences(DATABASE)
        return 'Thank you for using Music Recommender+. Have a good day.'
        #Go to save function and exit
    else:
        print('I\'m sorry, you have pressed an incorrect key. Please try again.')
    return continueToPrompt(name)

print(firstTimePrompt())