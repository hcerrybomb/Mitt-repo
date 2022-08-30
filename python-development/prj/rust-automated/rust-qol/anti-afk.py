from tkinter import E
from pynput.keyboard import * 
from time import time, ctime, sleep
keyboard = Controller()
x=0 
y=0
while x<19:
    keyboard.press('5')
    sleep(1)
    keyboard.release('5')
    sleep(1)
    keyboard.press(Key.space)
    sleep(1)
    keyboard.release(Key.space)
    sleep(1700)
    x = x + 1

while y<19:
    keyboard.press('4')
    sleep(1)
    keyboard.release('4')
    sleep(1)
    keyboard.press(Key.space)
    sleep(1)
    keyboard.release(Key.space)
    sleep(1700)
    y=y+1

while 1>0:
    keyboard.press('4')
    sleep(1)
    keyboard.release('4')
    sleep(1)
    keyboard.press(Key.space)
    sleep(1)
    keyboard.release(Key.space)
    sleep(1700)