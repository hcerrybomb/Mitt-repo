######                                                                      IMPORTS                 

import subprocess
from pynput.keyboard import *
from time import time, ctime, sleep
import pathlib
import os
import win32con
import sys
import win32gui
import win32process as wproc
import win32api as wapi

######                                                                      VARIABLE DECLARATIONS

os.system("")

keyboard = Controller()

__location__ = os.path.realpath(                                            #declares __location__ as a string of the path of this projects folder
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

programToFind = "Rust"

######                                                                      COLOR STYLING

class style():
    Red =       '\033[31m'
    Green =     '\033[32m'
    Yellow =    '\033[33m'
    Cyan =      '\033[36m'
    Underline = '\033[4m'
    Reset =     '\033[0m'

######                                                                      FIRST STATEMENT

def haveYou(input):
    if input == "Y" or input == "y" or input == "Yes" or input == "YES" or input == "yes":
        return True
    if input == "N" or input =="n" or input =="no" or input =="NO" or input == "No":
        return False
    else:
        return "invalid"

    

sleep(1)
print(style.Red+"\n================!!!IMPORTANT!!!================"+style.Reset)
sleep(0.5)
print("\n Step 1:\tFor the program to be its most efficient you should have the",style.Cyan,"Game Overlay",style.Reset,"Activity setting",style.Green,"Enabled",style.Reset,"on discord")
sleep(0.5)
print("\n Step 2:\tIf your game is open, make sure your screen mode is either borderless or windowed")
sleep(0.5)
print("\n        \tTo do this > open your game > open your menu > click OPTIONS > click SCREEN > set the screen MODE to either Borderless or Windowd > click APPLY CHANGES")
sleep(0.5)
screenModeInput = str(input("\n\n Is your screen mode correct? [Y/N] : "))
sleep(0.5)
while haveYou(screenModeInput) != True:
    if haveYou(screenModeInput)==False:
        print("\n Ok, please turn the setting on and restart the program")
        sleep(0.5)
        print("\n Program closing")
        sleep(3)
        raise SystemExit
    if haveYou(screenModeInput)=="invalid":
        print("\n Invalid input, try again")
        sleep(0.5)
        screenModeInput = str(input("\n\n Is your screen mode correct? [Y/N] : "))
sleep(0.5)
print("\n Step 3:\tMake sure you have a rust shortcut on your desktop, the program will now check this for you . . .")
sleep(2)
######                                                                      CHECK FOR RUST DESKTOP SHORTCUT

desktopPath = str(pathlib.Path.home() / 'Desktop')

rustShortcut = desktopPath + "\Rust.lnk"                                    #defines desktop variable for the shortcut

rawRustShortcut = r'%s ' %rustShortcut                                         #declares the full path for the placement of possible rust shortcut

if os.path.exists(rawRustShortcut) != True:                                    #checks if that path (aka the shortcut) exists
    print("\n there is",style.Red,"not",style.Reset,"a shortcut for rust present on your desktop, please create one and restart the program")
    sleep(0.5)
    print("\n Program closing")
    sleep(5)
    raise SystemExit

print("\n Rust shortcut",style.Green,"present",style.Reset,"on desktop, continuing program")
sleep(2)



projFolder = os.path.join(__location__)                                     #declares projFolder as path for this folder

projFolder = r'%s' %projFolder                                              #converts that into a real string

errorCheck = False                                                          #status for wether the users input is valid or not

######                                                                      FIRST STATEMENT

print(style.Cyan + "\n What time is wipe for you?"+style.Reset+"\n\n give your answer in an",style.Green,"00:00",style.Reset,"format")
sleep(0.5)
print("\n For example;\t13:20\t23:40\t17:00\t . . .")
sleep(0.5)

######                                                                      USER INPUT

wipeTimeInput = str(input("\n Give your answer here : "))                         #creates a variable for the users input
sleep(0.2)


while errorCheck == False:                                             #while the users input is invalid


    if len(wipeTimeInput)>5:                                                    #if there are too many characters in the user input

        print("\n"+style.Red+"Error :\t\t"+style.Reset+"Too many charcters")
        sleep(0.5)

        errorCheck = False                                             #user input stays invalid

        wipeTimeInput = str(input("\n Try again, give your answer here : "))               #user needs to give input again


    elif wipeTimeInput.count(":")<1:                                            #if there are no colons in the user input

        print(style.Red+"Error :\t\t"+style.Reset+"Missing colon")
        sleep(0.5)

        errorCheck = False                                             #user input stays invalid

        wipeTimeInput = str(input("\n Try again, give your answer here : "))               #user needs to give input again


    elif len(wipeTimeInput)<5:                                                  #if there are too few characters in the answer

        print(style.Red+"Error :\t\t"+style.Reset+" too few characters")
        sleep(0.5)

        errorCheck = False                                             #user input stays invalid

        wipeTimeInput = str(input("\n Try again, give your answer here:   "))               #user needs to give input again


    else:                                                                   #if none of the error conditions are met

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))           #declares __location__ as this folders path

        print(style.Green+"\n\n Wipe time saved succsessfully !"+style.Reset)
        sleep(0.5)
        print("\n\n The program will now initialize at the time of wipe,",style.Red,"do not",style.Reset,"close it")

        errorCheck = True                                              #user input is valid

wipeTime = str(wipeTimeInput)                                                     #declares the temp var as the users input

wipeTimeSplit = wipeTime.split(":")                                           #string stuff

wipeHour = wipeTimeSplit[0]

wipeMin = wipeTimeSplit[1]

integerWipeTime = str(wipeTimeSplit[0]+wipeTimeSplit[1])                      #4 letter string of the time of wipe

def getCurrentTime():                                                         #returns the time as a 4 letter string

    fullTime = time()                                                              #string stuff

    fullTimeString = str(ctime(fullTime))
    
    fullTimeStringSplit = fullTimeString.split(" ")
    
    clockTimes = fullTimeStringSplit[3].split(":")
    
    integerTime = str(clockTimes[0] + clockTimes[1])

    global currentHour

    currentHour = clockTimes[0]
    
    global currentMin

    currentMin = clockTimes[1]

    global currentSec

    currentSec = clockTimes[2]

    return integerTime

def getProcessStatus(process_name):                                           #function for checking if a process exists, arg is the full process name.exe    

    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    
    output = subprocess.check_output(call).decode()
    
    last_line = output.strip().split('\r\n')[-1]
    
    return last_line.lower().startswith(process_name.lower())

def connectToServer():                                                       #simulates key presses for connecting via console      TOTAL TIME PER 20.4 sec

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

def antiAfk():                                                             #simulates keypresses for not getting afk kicked         TOTAL TIME PER 20 sec
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

def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

windowsList = get_app_list()

numberOfWindows = len(windowsList)

while getCurrentTime() != integerWipeTime:                                    #while the return value of the WhatsTheTime function does not match the time of wipe, update the whats the time function

    getCurrentTime()

    currentHour = int(currentHour)
    wipeHour = int(wipeHour)
    currentMin = int(currentMin)
    wipeMin = int(wipeMin)
    currentSec = int(currentSec)

    if currentHour == wipeHour:

        if currentMin < wipeMin:

            HoursUntil = 0
            MinsUntil = wipeMin - currentMin

        if currentMin > wipeMin:

            HoursUntil = 23
            MinsUntil = (60 - currentMin) + wipeMin

    if currentHour < wipeHour:

        if currentMin < wipeMin:

            HoursUntil = wipeHour-currentHour
            MinsUntil = wipeMin - currentMin

        if currentMin > wipeMin:

            HoursUntil = (wipeHour - currentHour) - 1
            MinsUntil = (60 - currentMin) + wipeMin

    if currentHour > wipeHour:

        if currentMin < wipeMin:

            HoursUntil = (24 - currentHour) + wipeHour
            MinsUntil = wipeMin - currentMin

        if currentMin > wipeMin:

            HoursUntil = ((24 - currentHour) + wipeHour) - 1
            MinsUntil = (60 - currentMin) + wipeMin                 #fix minute wrong bug

    print("",HoursUntil,"Hrs",MinsUntil-1,"Mins",60-currentSec,"Seconds"," until Initialization",end = "\r")

    sleep(1)
print("\n Program starting . . .")
sleep(0.5)
print("\n Checking if Rust is open")
sleep(1)
if getProcessStatus('RustClient.exe') == True:                                #check if rust is open or not
    print("\n Rust is open")
    sleep(0.5)
    print("\n Locating window \n")
    sleep(0.5)
    for x in range(0,numberOfWindows):
        sleep(0.1)

        if programToFind == (str(windowsList[x]).split("'"))[1]:
            print("\tProgram nr\t",x,style.Green,"Match found\t",style.Reset,(str(windowsList[x]).split("'"))[1])
            correctProgram = (str(windowsList[x]).split("'"))[1]
        else:
            print("\tProgram nr\t",x,style.Red,"No match\t",style.Reset,(str(windowsList[x]).split("'"))[1])


    
    handle = win32gui.FindWindow(None, correctProgram)
    print("\n Hooking window")  
    if 1==1:
        try:
            
            win32gui.BringWindowToTop(handle)
            sleep(0.2)

            
            keyboard.press(Key.alt)
            win32gui.SetForegroundWindow(handle)
            sleep(0.5)

            keyboard.release(Key.alt)
            
            remote_thread, _ = wproc.GetWindowThreadProcessId(handle)
            wproc.AttachThreadInput(wapi.GetCurrentThreadId(), remote_thread, True)
            win32gui.SetFocus(handle)
            sleep(0.2)

            
            win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
            sleep(0.2)

            
            win32gui.BringWindowToTop(handle)
            sleep(0.2)

              
            win32gui.SetForegroundWindow(handle)
            sleep(0.2)

            
            win32gui.SetFocus(handle)
            sleep(0.2)
            print("\n Window hooked")
            sleep(1)
            

        except:

            print("\n",style.Yellow,"Expected error : ",style.Red,sys.exc_info(),style.Reset,"occurred")
            print("\n Program continuing")

    x=1
    print("\n Window hooked")
    sleep(0.2)
    print("\n Connecting to server . . .")
    connectToServer()
    sleep(1)
    print("\n Anti afk kicker will start in 20 minutes . . .")
    sleep(1200)
    while x<100:                                                            #runs connect and anti afk 100 times

        connectToServer()

        sleep(1)

        antiAfk()

        sleep(1)


        x=x+1
      
else:                                                                       #if it isnt open 
    print("\n Rust not open, opening Rust\n")
    print("\n")
    os.startfile(rawRustShortcut)                                                  #starts the DESKTOP SHORTCUT

    y=1

    while getProcessStatus('DiscordHookHelper64.exe') != True:                #checks 100 times if the discord hook is open, aka the game has reached main menu
        print("\n Checking if program is ready, check ", y, "/", "100",end="\r")
        if y < 100:

            sleep(0.5)

            y=y+1

        else:                                                               #if none of the 100 checks come back as true TIME OUT the checking

            print("\n Checker timed out, skipping check")

            break                         
    print("\n ")
    sleep(15)                                                               #waiting time to make sure the game boots up
    print("\n ")
    print("\n Locating window")
    windowsList = get_app_list()

    numberOfWindows = len(windowsList)
    for x in range(0,numberOfWindows):
        sleep(0.1)

        if programToFind == (str(windowsList[x]).split("'"))[1]:
            print("\tProgram nr\t",x,style.Green,"Match found\t",style.Reset,(str(windowsList[x]).split("'"))[1])
            correctProgram = (str(windowsList[x]).split("'"))[1]
        else:
            print("\tProgram nr\t",x,style.Red,"No match\t",style.Reset,(str(windowsList[x]).split("'"))[1])


    
    handle = win32gui.FindWindow(None, correctProgram)
    print("\n Hooking window")  
    if 1==1:
        try:
            
            win32gui.BringWindowToTop(handle)
            sleep(0.2)

            
            keyboard.press(Key.alt)
            win32gui.SetForegroundWindow(handle)
            sleep(0.5)

            keyboard.release(Key.alt)
            
            remote_thread, _ = wproc.GetWindowThreadProcessId(handle)
            wproc.AttachThreadInput(wapi.GetCurrentThreadId(), remote_thread, True)
            win32gui.SetFocus(handle)
            sleep(0.2)

            
            win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE)
            sleep(0.2)

            
            win32gui.BringWindowToTop(handle)
            sleep(0.2)

              
            win32gui.SetForegroundWindow(handle)
            sleep(0.2)

            
            win32gui.SetFocus(handle)
            sleep(0.2)
            print("\n Window hooked")
            sleep(1)
            

        except:

            print("\n",style.Yellow,"Expected error : ",style.Red,sys.exc_info(),style.Reset,"occurred")
            print("\n Program continuing")
                                                                #when its up, focus the tab

    print("\n Connecting to server")
    connectToServer()                                                        #runs the connect server function
    sleep(1)
    x=1
    print("\n Anti afk kicker will start in 20 minutes . . .")
    sleep(1200)
    while x<100:                                                            #runs connect and anti afk 100 times

        connectToServer()

        sleep(1)

        antiAfk()

        sleep(1)

        x=x+1