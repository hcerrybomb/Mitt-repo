import random

from turtle import *

antall = int(input("Hva er antallet: "))

tall = random.randint(1, 10)

startJaNei = 0

pensize(5)



AntallLeft = 0

def RightOrLeft(LeftRight):
    
    
    if LeftRight == 1:
        right(90)
        
        global AntallRight
        
        AntallRight = AntallRight + 1
    if LeftRight == 2:
        left(90)
        AntallLeft = AntallRight + 1



while startJaNei < antall:
    tall = random.randint(1, 10)
    ForwardLenght = random.randint(10,30)
    
    LeftRight = random.randint(1,2)
    

    
    
    if tall == 1:
        color("#f600f6")
        forward(ForwardLenght)
        
        RightOrLeft(LeftRight)
        
    if tall == 2:
        color("#e200e2")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 3:
        color("#ce00ce")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 4:
        color("#bb00bb")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 5:
        color("#a700a7")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 6:
        color("#940094")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 7:
        color("#800080")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 8:
        color("#6c006c")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 9:
        color("#590059")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    if tall == 10:
        color("#450045")
        forward(ForwardLenght)
        RightOrLeft(LeftRight)
    startJaNei = startJaNei + 1
                            



