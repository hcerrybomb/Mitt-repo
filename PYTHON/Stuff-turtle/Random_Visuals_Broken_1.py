import random
from turtle import *
antall = int(input("Antall streker: "))
tall = random.randint(1, 10)
startJaNei = 0
pensize(2)
AntallRight = 0
AntallLeft = 0
def RightOrLeft(LeftRight):
    left(90)
    if LeftRight == 1:
        global AntallRight
        if AntallRight > 0:
            left(90)
            AntallRight = 0
        else:
            right(90)
            AntallRight = AntallRight + 1
    if LeftRight == 2:
        global AntallLeft
        if AntallLeft > 2:
            right(90)
            AntallLeft = 0
        else:
            left(90)
            AntallLeft = AntallLeft + 1
            
colormode(255)
     
red = 1
green = 0
blue = 0



while startJaNei < antall:
    
    
    farge = (red, green, blue)
    
    tall = random.randint(1, 10)
    ForwardLenght = random.randint(30,50)
    ForwardLenght = ForwardLenght +1
    LeftRight = random.randint(1,2)
    if tall == 1:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 2:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 3:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 4:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 5:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 6:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 7:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 8:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 9:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 10:
        color(farge)
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    startJaNei = startJaNei + 1
    if red < 254:
        red = red + 1
    elif red >= 254:
        if green == 0:
            green = green + 1
    if 255 > green > 0:
        green = green + 1
    elif green >= 255:
        if blue == 0:
            blue = blue + 1
    if 254 > blue > 0:
        blue = blue + 1