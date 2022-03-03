import random
from turtle import *
antall = int(input("Antall streker: "))
counter = 0
startJaNei = 0
pensize(2)
def RightOrLeft(LeftRight):
    left(90)
   # if LeftRight == 1:
    #    global AntallRight
     #   if AntallRight > 0:
      #      left(90)
       #     AntallRight = 0
  #      else:
   #         right(90)
    #        AntallRight = AntallRight + 1
  #  if LeftRight == 2:
   #     global AntallLeft
    #    if AntallLeft > 2:
     #       right(90)
      #      AntallLeft = 0
       # else:
        #    left(90)
         #   AntallLeft = AntallLeft + 1
    
color("white")
goto(-680,300)

            
colormode(255)
     
rød = 1
grønn = 0
blå = 0

y1 = 280

while startJaNei < antall:
    right(90)
    forward(30)
    left(90)
    forward(2)
    left(90)
    
    farge = (rød, grønn, blå)
    color(farge)
    
   
    startJaNei = startJaNei + 1
    if rød < 254:
        rød = rød + 1
    elif rød >= 254:
        if grønn == 0:
            grønn = grønn + 1
    if 255 > grønn > 0:
        grønn = grønn + 1
    elif grønn >= 255:
        if blå == 0:
            blå = blå + 1
    if 254 > blå > 0:
        blå = blå + 1
    forward(28)
    right(90)
    forward(2)
    
    counter = counter + 4
    
    if counter % 1360 == 0:
        goto(-680,y1)
        y1 = y1 - 20
        