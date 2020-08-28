from Shapes import *

if __name__ == '__main__':
    face = Circle(Vector(0, -200), 200, 'yellow')
    face.render()
    left_eye = Circle(Vector(-60, 50), 40, 'black')
    left_eye.render()
    right_eye = Circle(Vector(60, 50), 40, 'black')
    right_eye.render()
    mouth = Circle(Vector(0, -150), 50, 'red')
    mouth.render()

eqtri = EqualateralTriangle(300,Vector(0,0),'black')
print(eqtri.render())
rectan = Rectangle(4,5,Vector(2,4),'black')
print(rectan.render())
squa = Square(4,Vector(5,-2),'black')
print(squa.render())
cir = Circle(Vector(12,9),14)
print(cir.render())
