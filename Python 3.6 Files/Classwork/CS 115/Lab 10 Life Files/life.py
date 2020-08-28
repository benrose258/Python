#
# life.py - Game of Life lab
#
# Name:Ben Rose
# Pledge:I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width,height):
    '''Returns a 2d array with "height" rows and "width" cols.'''
    board = []
    for row in range(height):
        board += [createOneRow(width)]
    return board

def printBoard(board):
    '''This function prints the 2d list-of-lists board without spaces (using sys.stdout.write)'''
    for row in board:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    board = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                board[row][col] = 1
            else:
                board[row][col] = 0
    return board

def innerCells(width,height):
    counter = 1
    board = []
    for number in range(height):
        if counter > height:
            break
        elif counter == 1 or counter == height:
            board.append([0*width])
        else:
            board.append([[0] + [1]*(width-2) + [0]])
        counter += 1
    return board

def random2Cells(width,height):
    counter = 1
    board = []
    for number in range(height):
        if counter > height:
            break
        elif counter == 1 or counter == height:
            board.append([[0]*width])
        else:
            widthCounter = 1
            widthList = []
            for number in range(width-2):
                widthList.append(random.choice([0,1]))
            board.append([[0] + widthList + [0]])
        counter += 1
    return board

def randomCells(w, h):
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range (1, w - 1):
            A[row][col] = random.choice([0, 1])
    return A

def copy(board):
    #Creates a deep copy of a board
    newBoard = createBoard(len(board[0]),len(board))
    for row in range(len(board)):
        for col in range(len(board[0])):
            newBoard[row][col] = board[row][col]
    return newBoard

def innerrReverse(board):
    newBoard = copy(board)
    reversedBoard = []
    counter = 1
    height = len(board)
    width = len(board[0])
    for number in range(height):
        if counter > height:
            break
        elif counter == 1 or counter == height:
            counter += 1
            reversedBoard.append([board[0]])
        else:
            widthCounter = 1
            oldBody = board[number][1:-1]
            newBody = []
            for number in range(width-2):

                if oldBody[widthCounter] == 0:
                    widthCounter += 1
                    newBody.append('1')
                else:
                    newBody.append('0')
            reversedBoard.append([['0'] + newBody + ['0']])
        counter += 1
    return reversedBoard

def innerReverse(board):
    for row in range(1, len(board) - 1):
        for col in range(1, len(board[0]) - 1):
            if board[row][col] == 0:
                board[row][col] = 1
            else:
                board[row][col] = 0
    return board

def countNeighbors(row,col,board):
    neighborList = [board[row-1],board[row],board[row+1]]
    lastList = []
    for index in neighborList:
        lastList.append(index[col-1:col+2])
    mysum = 0
    for index in lastList:
        for subindex in index:
            mysum += subindex
    return mysum - lastList[1][1]

def next_life_generation(board):
    newBoard = copy(board)
    for row in range(1, len(board) - 1):
        for col in range(1, len(board[0]) - 1):
            if newBoard[row][col] == 0 and countNeighbors(row, col, board) == 3:
                newBoard[row][col] = 1
            elif 2 > countNeighbors(row,col,board) or countNeighbors(row, col, board) > 3:
                newBoard[row][col] = 0
            else:
                pass
    return newBoard

board = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
printBoard(board)
print()
board2 = next_life_generation(board)
printBoard(board2)
print()
board3 = next_life_generation(board2)
printBoard(board3)
