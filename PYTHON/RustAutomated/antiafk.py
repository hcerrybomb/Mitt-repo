from pynput.keyboard import *
from time import time, ctime, sleep
keyboard = Controller()
while 1>0:
    keyboard.press('w')
    keyboard.tap(Key.space)
    sleep(1500)