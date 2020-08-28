'''
Created on May 1, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
'''

class Board(object):
    def __init__(self,width=7,height=6):
        '''Takes in the width of the board, the height of the board, and creates the board.'''
        self.width = width
        self.height = height
        boardList = []
        oneBoard = [' ']
        for index in range(height):
            boardList.append(oneBoard * width)
        self.boardList = boardList

    def boardList(self):
        '''boardlist property'''
        return self.boardList

    def boardList(self,boardList):
        '''boardlist setter'''
        self.boardList = boardList

    def allowsMove(self,columnNum):
        '''checks if a move is allowed (column is not full and exists) in the column columnNum'''
        if columnNum > self.width-1:
            return False
        for index in self.boardList[columnNum]:
            if index == ' ':
                return True
        return False

    def addMove(self,columnNum,ox):
        '''Adds an x or an o to the first available space in the column columnNum'''
        counter = self.height - 2
        while counter >= 0:
            if self.boardList[counter][columnNum] == ' ':
                self.boardList[counter][columnNum] = ox
                return Board()
            else:
                counter -= 1


    def setBoard(self,moveString):
        '''Modifies the board with the inputs in moveString'''
        '''moveString: The current moves between x's and o's, so 00123 would be x in the bottom left, o right above it,
           x on the bottom in row 1, 0 on the bottom in row 2, and x in the bottom of row 3.'''
        nextChecker = 'X'
        for move in moveString:
            curSpace = int(move)
            self.addMove(curSpace,nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def delMove(self,column):
        '''Deletes moves from the board'''
        if [' '] * self.width != column:
            for index in range(len(column)):
                if column[index] != ' ':
                    column[index] = ' '
                    return column

    def winsFor(self,ox):
        '''Calculates for vertical,horizontal, and both diagonals if a player has won'''
        counter = 0
        for row in range(self.width):
            counter = 0
            for column in range(self.height):
                if counter == 4:
                    return True
                if self.boardList[row][column] == ox:
                    counter += 1
                else:
                    counter = 0

        for column in range(self.height):
            counter = 0
            for space in range(self.width):
                if counter == 4:
                    return True
                if self.boardList[column][row] == ox:
                    counter += 1
                else:
                    counter = 0
        #0,0 1,1 2,2 3,3
        #1,0 2,1 3,2 4,3
        #...
        for heightval in range(self.height-4):
            counter = 0
            for space in range(self.width-4):
                counter = 0
                #Next loop checks the adding for each diagonal
                for number in range(4):
                    if counter == 4:
                        return True
                    if self.boardList[heightval + number][space + number] == ox:
                        counter += 1
                    else:
                        counter = 0
                        break

        for heightval in range(-1,-self.height+4):
            counter = 0
            for space in range(self.width-4):
                counter = 0
                #Next loop checks the adding for each diagonal, so does 1 diagonal at a time, so if it doesnt work, break
                for number in range(4):
                    if counter == 4:
                        return True
                    if self.boardList[heightval - number][space + number] == ox:
                        counter += 1
                    else:
                        counter = 0
                        break
        return False

    def hostGame(self):
        '''Begins (what was going to be) the connect 4 game.'''
        print('Welcome to Connect Four!\n')
        print(Board())
        print()
        colChoice = int(input('Xs choice: '))
        if self.allowsMove(colChoice) == True:
            self.setBoard(str(colChoice))
            print(Board())
        else:
            print('error')

    def __str__(self):
        '''Creates and returns boardList in string form, which includes the formatting for the board (e.g. dashes and numbers at the bottom)'''
        boardString = '|'
        indexnum = 0
        while indexnum < len(self.boardList):
            for index in range(len(self.boardList[indexnum])):
                boardString += self.boardList[indexnum][index] + '|'
            indexnum += 1
            boardString += '\n'
            if indexnum != len(self.boardList):
                boardString += '|'
        boardString += '-' * (1 + 2 * self.width) + '\n'
        for number in range(self.width):
            boardString += ' ' + str(number)
        return boardString

checkers = Board(7,6)
print(checkers.hostGame())
