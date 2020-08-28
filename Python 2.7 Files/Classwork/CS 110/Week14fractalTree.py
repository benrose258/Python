# Week 14 drawing fractal trees


import turtle

branchLen =200

def fractalTree(trunkLen):
    '''Recursively draw a tree given a starting trunk length'''
    if trunkLen < 10: return
    else:
        turtle.forward(trunkLen)
        turtle.left(45)
        fractalTree(trunkLen/2)
        turtle.right(90)
        fractalTree(trunkLen/2)
        turtle.left(45)
        turtle.backward(trunkLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.color("blue")
    fractalTree(branchLen)    
    myWin.exitonclick()
    

main()
