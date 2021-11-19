######      IMPORTS                 

import subprocess
from pynput.keyboard import *
from time import time, ctime, sleep
import pathlib
import os

######       VARIABLE DECLARATIONS

os.system("") 
keyboard = Controller()
e=str
__location__ = os.path.realpath(        #declares __location__ as a string of the path of this projects folder
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

######      COLOR STYLING

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

######      FIRST STATEMENT

print(style.RED+"\n!!!IMPORTANT!!!"+style.RESET)

print("\nYou MUST have the"+style.YELLOW+" GAME OVERLAY"+style.RESET+" activity setting in"+style.YELLOW+" DISCORD  "+style.UNDERLINE+"ENABLED"+style.RESET+"  for this program to work")

######      CHECK FOR RUST DESKTOP SHORTCUT

desktop = str(pathlib.Path.home() / 'Desktop') + "\Spyder (Anaconda3).lnk"   #is meant to be + "\Rust.lnk"

desktop = r'%s ' %desktop               #declares the full path for the placement of possible rust shortcut

if os.path.exists(desktop) == True:     #checks if that path (aka the shortcut) exists

    print("desktop shortcut present")


else:

    print("desktop shortcut not present")

    
######

projFolder = os.path.join(__location__) #declares projFolder as path for this folder

projFolder = r'%s' %projFolder          #converts that into a real string









            #checks if content is NotConfig'd, which is its default state beofre the txtfilehandler changes it

UserInputStatus = False     #status for wether the users input is valid or not

######      FIRST STATEMENT

print(style.CYAN + "\nwhat time is wipe for you?"+style.RESET+"\n\ngive your answer in an 00:00 format\n\nexamples:\n\n    17:00\n    15:30\n    04:45\n\n")

######      USER INPUT

UserInput = str(input("give your answer here:   "))     #creates a variable for the users input

while UserInputStatus == False:     #while the users input is invalid


    if len(UserInput)>5:            #if there are too many characters in the user input

        print("\n"+style.RED+"Error:"+style.RESET+" Too many charcters\n\ntry again")

        UserInputStatus = False     #user input stays invalid

        UserInput = str(input("\ngive your answer here:   "))   #user needs to give input again


    elif UserInput.count(":")<1:    #if there are no colons in the user input

        print(style.RED+"Error:"+style.RESET+" Missing colon\n\ntry again")

        UserInputStatus = False     #user input stays invalid

        UserInput = str(input("\ngive your answer here:   "))   #user needs to give input again


    elif len(UserInput)<5:          #if there are too few characters in the answer

        print(style.RED+"Error:"+style.RESET+" too few characters\n\ntry again")

        UserInputStatus = False     #user input stays invalid

        UserInput = str(input("\ngive your answer here:   "))   #user needs to give input again


    else:   #if none of the error conditions are met

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))   #declares __location__ as this folders path

        print(style.GREEN+"\n\nwipe time saved succsessfully"+style.RESET)

        UserInputStatus = True      #user input is valid






wipeTime=UserInput            #makes var for the temp var

tempVar = str(wipeTime)                 #declares the temp var as the users input

print("program will initiate at: ",tempVar,"until then, dont close the process")

tempVarSplit = tempVar.split(":")       #string stuff

tempVarHour =tempVarSplit[0]

tempVarMin =tempVarSplit[1]

tempVarCombined = str(tempVarSplit[0]+tempVarSplit[1])  #4 letter string of the time of wipe


def WhatsTheTime():             #returns the time as a 4 letter string

    t = time()                          #string stuff

    b = str(ctime(t))
    
    c= b.split(" ")
    
    d= c[3].split(":")
    
    e = str(d[0] + d[1])
    global CurrentHour
    CurrentHour =d[0]
    
    global CurrentMin
    CurrentMin =d[1]
    global CurrentSec
    CurrentSec =d[2]

    return e

def process_exists(process_name):       #function for checking if a process exists, arg is the full process name.exe    

    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    
    output = subprocess.check_output(call).decode()
    
    last_line = output.strip().split('\r\n')[-1]
    
    return last_line.lower().startswith(process_name.lower())

def connect_server():       #simulates key presses for connecting via console

    keyboard.press(Key.f1)      #open console
    sleep(0.2)
    keyboard.release(Key.f1)

    sleep(5)                    #lag timer

    keyboard.type("connect 164.132.200.22:28026")   #connects to server
    sleep(10)                   #lag time
    keyboard.tap(Key.enter)                         #executes

    sleep(5)                    #lag time

    keyboard.press(Key.f1)  #close console
    sleep(0.2)
    keyboard.release(Key.f1)

def anti_afk():         #simulates keypresses for not getting afk kicked

    keyboard.press('w') 
    keyboard.tap(Key.space)
    sleep(5)
    keyboard.release('w')

    keyboard.press('a')
    keyboard.tap(Key.space)
    sleep(5)
    keyboard.release('a')

    keyboard.press('s')
    keyboard.tap(Key.space)
    sleep(5)
    keyboard.release('s')

    keyboard.press('d')
    keyboard.tap(Key.space)
    sleep(5)
    keyboard.release('d')




while WhatsTheTime() != tempVarCombined:

    CurrentHour = int(CurrentHour)
    tempVarHour = int(tempVarHour)
    CurrentMin = int(CurrentMin)
    tempVarMin = int(tempVarMin)
    CurrentSec = int(CurrentSec)


    if CurrentHour == tempVarHour:
        if CurrentMin < tempVarMin:
            HoursUntil = 0
            MinsUntil = tempVarMin - CurrentMin

        if CurrentMin > tempVarMin:
            HoursUntil = 23
            MinsUntil = (60-CurrentMin)+tempVarMin
    if CurrentHour < tempVarHour:


    14:25 current
    14:10 temp
    ss









    print("current hour:\t",CurrentHour,"\tcurrent min\t",CurrentMin,"\tcurrent second\t",CurrentSec)
    print("wipe hour:\t",tempVarHour,"\twipe min:\t",tempVarMin)
    
    
    sleep(1)
    WhatsTheTime()
    
print("wipe time reached, program initiating...")
sleep(1)
print("checking if rust is open or not")
sleep(1)
if process_exists('pythonw.exe') == True:   #is meant to be 'RustClient.exe
    print("rust is open")
    sleep(1)
    print("Rust hooked")
    sleep(1)


    import focus


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
    while process_exists('DiscordHookHelper64.exe') != True:  #can just leave for testing since it has a timed out timer
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

    import focus
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
