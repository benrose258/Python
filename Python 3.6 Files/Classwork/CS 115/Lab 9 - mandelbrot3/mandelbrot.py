# mandelbrot.py
# Lab 9
#
# Name: Ben Rose
# I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,mynumber):
    result = 0
    for number in range(mynumber):
        result = result + c
    return result

def update(c,mynumber):
    z = 0
    for number in range(mynumber):
        z = z**2 + c
    return z

def inMSet(c,mynumber):
    z = 0
    for number in range(mynumber):
        if abs(z) > 2:
            return False
        else:
            z = z**2 + c
    return True

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col%10 == 0 and row%10 == 0:
        return True
    else:
        return False
def test():
    '''If you change from and to or, the function will contain a grid
       instead of a series of dots.'''
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()

def scale(pix,pixMax,floatMin,floatMax):
    scaleValue = pix/pixMax
    howFar = abs(floatMin) + abs(floatMax)
    return floatMin + howFar * scaleValue

def mset():
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            x = scale(col,300,-2.0,1.0)
            y = scale(row,200,-1.0,1.0)
            c = x + y*1j
            if inMSet(c,25) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
