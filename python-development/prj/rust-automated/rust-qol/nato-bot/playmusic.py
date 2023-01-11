from tkinter import E
from pynput.keyboard import * 
from time import time, ctime, sleep
keyboard = Controller()
sleep(10)
keyboard.press(' ')
sleep(60000)
keyboard.release('v')