import subprocess
from pynput.keyboard import *
from time import time, ctime, sleep
import pathlib
import os
import win32gui

os.system("") #to fix the color somehow
keyboard = Controller()
#C:\Users\Gaming Dator VII\Desktop
#C:\Users\Gaming Dator VII\Desktop\Mitt-repo\PYTHON

#use os command to install pip keyboard

#press esc 3 time to close sidebar,task manager etc

e=str
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BLINK = '\33[5m'

print( style.RED + "\n!!!IMPORTANT!!!" + style.RESET)
print("\nYou MUST have the"+style.YELLOW+" GAME OVERLAY"+style.RESET+" activity setting in"+style.YELLOW+" DISCORD  "+style.UNDERLINE+"ENABLED"+style.RESET+"  for this program to work")





desktop = pathlib.Path.home() / 'Desktop'

desktop = str(desktop)
desktop = desktop + "\Rust.lnk"

desktop = r'%s ' %desktop

if os.path.exists(desktop) == True:
    print("desktop shortcut present")
else:
    print("desktop shortcut not present")




batLocation = os.path.join(__location__, 'nonsecureSendKeys.bat')

batLocation = r'%s ' %batLocation


projFolder = os.path.join(__location__)


projFolder = r'%s' %projFolder

print(projFolder)
os.system('cd '+projFolder)
os.system('python txtFileLocationHandler.py')
WipeTimeInputPath=projFolder+'\WipeTimeInput.txt'
print(WipeTimeInputPath)
txtFileRead = open(WipeTimeInputPath, "r")
txtfilecontent = txtFileRead.read()

while txtfilecontent == "NotConfig":
    sleep(1)
    print("not ready yet")

print("what local time is wipe for you?")

print("the format is 00:00")


#WipeTime = str(input("type the time here : "))
wipeTime="12:12"

wipeTime = wipeTime.split(":")

wipeHR = int(wipeTime[0])

wipeMIN = int(wipeTime[1])



wipeTime = str(wipeTime[0] + wipeTime[1])

print("your wipe time is: ",wipeTime)

def WhatsTheTime():

    t = time()

    b = str(ctime(t))
    
    c= b.split(" ")
    
    d= c[3].split(":")
    
    e = str(d[0] + d[1])

    print("program initiation: ",wipeHR,":",wipeMIN,"\n","current time:       ",d[0],":",d[1],":",d[2],end="\r")

    return e

def process_exists(process_name):

    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    
    output = subprocess.check_output(call).decode()
    
    last_line = output.strip().split('\r\n')[-1]
    
    return last_line.lower().startswith(process_name.lower())

def connect_server():

    keyboard.press(Key.f1)
    sleep(0.2)
    keyboard.release(Key.f1)

    sleep(5)

    keyboard.type("connect 164.132.200.22:28026")
    sleep(10)
    keyboard.tap(Key.enter)

    sleep(5)

    keyboard.press(Key.f1)
    sleep(0.2)
    keyboard.release(Key.f1)

def anti_afk():

    keyboard.press(Key.w) #fix wrong 
    sleep(5)
    keyboard.release(Key.w)

    keyboard.press(Key.a)
    sleep(5)
    keyboard.release(Key.a)

    keyboard.press(Key.s)
    sleep(5)
    keyboard.release(Key.s)

    keyboard.press(Key.d)
    sleep(5)
    keyboard.release(Key.d)
    sleep(1)
    keyboard.tap(Key.space)

def focus_rust():

    subprocess.call([batLocation, "Rust", ""]) #add support for focusin when minimized

    print("rust focused")

while WhatsTheTime() != wipeTime:

    WhatsTheTime()
    
    sleep(1)
    
print("wipe time reached, program initiating...")
sleep(1)
print("checking if rust is open or not")
sleep(1)
if process_exists('RustClient.exe') == True:
    print("rust is open")
    sleep(1)
    print("Rust hooked")
    sleep(1)
    focus_rust()
    print("focused rust tab")
    sleep(1)
    print("starting server connection")
    connect_server()
    print("starts the script for continuing to connect and anti-afk")
    x=1
    while x<100:
        connect_server()
        sleep(1)
        anti_afk()

        x=x+1

        print("ur no longer afk")
        sleep(1)

else:
    
    os.startfile (desktop)
    y=1
    while process_exists('DiscordHookHelper64.exe') != True:
        if y < 100:
            y=y+1

            print("program not ready yet")
            sleep(0.5)
        else:
            print("ready checker timed out")
            break
    print("Rust hooked")
    print("waiting incase its still booting up")
    sleep(20)

    focus_rust()
    print("focused rust tab")
    print("starting server connection")
    connect_server()
    
    print("starts the script for continuing to connect and anti-afk")
    x=1
    while x<100:
        connect_server()
        sleep(1)
        anti_afk()

        x=x+1

        print("ur no longer afk")
        sleep(1)
