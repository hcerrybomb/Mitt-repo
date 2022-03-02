import csv
import os 
from pynput import keyboard
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
listOfCodes = []
def itemstr(row):
    stri = ""
    for ele in row:
        stri += ele
    return stri
with open(os.path.join(__location__, 'codefreq.csv')) as file:
    reader = csv.reader(file)
    for row in reader:
        del row[1]
        row = itemstr(row)
        listOfCodes.append(row)