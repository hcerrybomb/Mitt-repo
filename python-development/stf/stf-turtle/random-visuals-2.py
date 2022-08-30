import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas
import random
def zoom(event):
    amount = 0.9 if event.delta < 0 else 1.1
    canvas.scale(tk.ALL, 0, 0, amount, amount)
root = tk.Tk()
canvas = ScrolledCanvas(master=root, width=2000, height=2000)
canvas.pack(fill=tk.BOTH, expand=tk.YES)
screen = TurtleScreen(canvas)
turtle = RawTurtle(screen)
screen.delay(0.1)
turtle.goto(0,0)
screen.colormode(255)
red=2
green=4
blue=3
screen.bgcolor("black")
#screen.screensize(canvheight=30000, canvwidth=60000)
NumberOfLines =10000
turtle.color(red, green, blue)
turtle.forward(0)
LenForward = random.randint(50,70)
PenSizeNumber = 2
NumRight = 0
NumLeft = 0
while NumberOfLines > 0:
    NumberOfLines = NumberOfLines
    if PenSizeNumber == 10:
        PenSizeNumber = 9
    elif PenSizeNumber == 3:
        PenSizeNumber = 4
    elif PenSizeNumber%2==0:
        PenSizeNumber = PenSizeNumber + 2
    elif PenSizeNumber%2==1:
        PenSizeNumber = PenSizeNumber - 2
    turtle.pensize(PenSizeNumber)
    LenForward = random.randint(15,30)
    LeftOrRight = 0
    LeftOrRight = random.randint(1,2)
    PenSizeNumber = PenSizeNumber / 2
    if LeftOrRight== 1:
        LeftOrRight = turtle.left(90)
        NumLeft = NumLeft + 1
    if LeftOrRight== 2:
        LeftOrRight = turtle.right(90)
        NumRight = NumRight + 1
    if LeftOrRight== 3:
        LeftOrRight = turtle.left(45)
        NumLeft = NumLeft + 1
    if LeftOrRight== 4:
        LeftOrRight = turtle.right(45)
        NumRight = NumRight + 1
#    if NumLeft == 4:
#       LeftOrRight = right(90)
#        NumLeft = 0
#    if NumRight == 4:
#        LeftOrRight = left(90)
#        NumRight = 0
    turtle.forward(LenForward)
    LeftOrRight
    ColorPicker = random.randint(1,3)
    PlusOrMinus = random.randint(-2,3)
    if red < 3 or green < 3 or blue < 3:
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
    turtle.color(red, green, blue)
    print(red, green, blue)
    PenSizeNumber = PenSizeNumber * 2
    if red + green + blue >743:
        break
#turtle.done()
canvas.bind('<MouseWheel>', zoom)
screen.mainloop()