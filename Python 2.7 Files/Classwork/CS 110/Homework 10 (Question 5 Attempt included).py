#I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose
#Homework 10

#Question 1

Q1 = (1,(2,(6,(),()),(3,(5,(),()),(9,(),()))),(7,(8,(),()),(6,(),())))

#Question 2

def leaf(Tree):
    if Tree[1] == () and Tree[2] == ():
        return True
    else:
        return False

def sumTree(Tree):
    if Tree == ():
        return 0
    else:
        if leaf(Tree) == True:
            return Tree[0]
        else:
            return Tree[0] + sumTree(Tree[1]) + sumTree(Tree[2])

#Question 3

def listAll(Tree):
    if Tree == ():
        return []
    elif leaf(Tree) == True:
        return [Tree[0]]
    else:
        return [Tree[0]] + listLeaves(Tree[1]) + listLeaves(Tree[2])

def listLeaves(Tree):
    if Tree == ():
        return []
    else:
        return [Tree[0]] + listLeaves(Tree[1]) + listLeaves(Tree[2])

def averageTree(Tree):
    if Tree == ():
        return 0
    else:
        if leaf(Tree) == True:
            return Tree[0]
        else:
            return (Tree[0] + sumTree(Tree[1]) + sumTree(Tree[2]))/len(listAll(Tree))

#Question 4

def mirrorTree(Tree):
    if leaf(Tree) == True:
        return Tree
    else:
        root = Tree[0]
        Left = Tree[1]
        Right = Tree[2]

        LeftRoot = Left[0]
        LeftLeft = Left[1]
        LeftRight = Left[2]

        RightRoot = Right[0]
        RightLeft = Right[1]
        RightRight = Right[2]

        newLeft = (LeftRoot,LeftRight,LeftLeft)
        newRight = (RightRoot,RightRight,RightLeft)
        newTree = (root,newRight,newLeft)
        return newTree

#Question 5

import turtle

branchLen = 50

def drawLeaf(number,t):
    t.write(number[0], font=("Arial",16, "normal"))

def drawTree(number,t):
    t.ht() #hide turtle
    if number[1] == ():
        drawLeaf(number,t)
    else:
        t.left(30)
        t.forward(branchLen)
        drawTree(number[1],t)
        t.backward(branchLen)
        t.right(60)
        t.forward(branchLen)
        drawTree(number[2],t)
        t.backward(branchLen)
        t.left(30)
        drawTree(number[3],t)
        t.backward(branchLen)
        t.right(60)
        t.forward(branchLen)

def main():
    t = turtle.Turtle()
    myWindow = turtle.Screen()
    t.color("blue")
    drawTree(('root',('root',('A', (), ()),('B', (), ())) ,('root',('C', (6,(),()), (7,(),()))),('D', (5,(),()), (6,(),()))),t)
    myWindow.exitonclick()
