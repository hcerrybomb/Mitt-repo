from tkinter import E
from pynput.keyboard import * 
from time import time, ctime, sleep
keyboard = Controller()
while 1>0:
    keyboard.press('c')
    sleep(1)
    keyboard.release('c')
    sleep(1)
    keyboard.press(Key.space)
    sleep(1)
    keyboard.release(Key.space)
    sleep(2000)