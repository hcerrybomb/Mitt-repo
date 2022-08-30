from turtle import *
import random
delay(0.1)
goto(0,0)
colormode(255)
red=1
green=0
blue=0
bgcolor("black")
screensize(canvheight=30000, canvwidth=60000)
NumberOfLines =10000
color(red, green, blue)
forward(0)
LenForward = random.randint(30,50)
PenSizeNumber = 2
NumRight = 0
NumLeft = 0

while NumberOfLines > 0:
    if PenSizeNumber == 10:
        PenSizeNumber = 9
    elif PenSizeNumber == 3:
        PenSizeNumber = 4
    elif PenSizeNumber%2==0:
        PenSizeNumber = PenSizeNumber + 2
    elif PenSizeNumber%2==1:
        PenSizeNumber = PenSizeNumber - 2
    pensize(PenSizeNumber)
    LenForward = random.randint(15,30)
    LeftOrRight = 0
    LeftOrRight = random.randint(1,4)

    if LeftOrRight== 1:
        LeftOrRight = left(90)
        NumLeft = NumLeft + 1
    if LeftOrRight== 2:
        LeftOrRight = right(90)
        NumRight = NumRight + 1
    if LeftOrRight== 3:
        LeftOrRight = left(45)
        NumLeft = NumLeft + 1
    if LeftOrRight== 4:
        LeftOrRight = right(45)
        NumRight = NumRight + 1

#    if NumLeft == 4:
#       LeftOrRight = right(90)
#        NumLeft = 0
#    if NumRight == 4:
#        LeftOrRight = left(90)
#        NumRight = 0

    forward(LenForward)
    LeftOrRight
    ColorPicker = random.randint(1,3)
    PlusOrMinus = random.randint(-2,2)
    if red < 2 or green < 2 or blue < 2:
        PlusOrMinus = 3
    if ColorPicker == 1:
        if red < 249:
            red = red + PlusOrMinus
        elif red >= 249:
            red = red
    elif ColorPicker == 2:
        if green < 249:
            green = green + PlusOrMinus
        elif green >= 249:
            green = green       
    elif ColorPicker == 3:
        if blue < 249:
            blue = blue + PlusOrMinus
        elif blue >= 249:
            blue = blue
    color(red, green, blue)
    print(red, green, blue)
    if red + green + blue >743:
        break


    




done()