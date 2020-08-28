'''
Created on Feb 16, 2017

@author: Ben Rose
'''
import turtle

def squareSpiral(walls):
    def squareSpiralHelper(distance,initial,count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(90) #Moves the turtle left 90 degrees
            turtle.forward(distance)
            return squareSpiralHelper(distance+initial * (count % 2),initial,count+1)

    squareSpiralHelper(20,20,0)

squareSpiral(30)
