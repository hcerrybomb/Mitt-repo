import subprocess
from pynput.keyboard import *
from time import time, ctime, sleep
import os

keyboard = Controller()
#C:\Users\Gaming Dator VII\Desktop
#C:\Users\Gaming Dator VII\Desktop\Mitt-repo\PYTHON
e =str
sleep(1)
print(" ")
print("")
print("!!!IMPORTANT!!! you MUST have the GAME OVERLAY activity setting in DISCORD  ENABLED  for this program to work")
print(" ")
sleep(1)
print("continuing program")
print(" ")
sleep(5)
print("the program needs the file path location of 1:")
sleep(1)
print(" ")
print("your rust shortcut .lnk file, AKA your rust desktop shortcut")
sleep(1)
print(" ")
print("this will typically look something like  C:\\Users\\YourUserName\\Desktop ")
sleep(1)
print(" ")
print("to find this:")
sleep(1)
print(" ")
print(">  find  the Rust shortcut  on your Desktop ")
sleep(0.3)
print(">  right click  it")
sleep(0.3)
print(">  click  properties")
sleep(0.3)
print(">  click  the 'General' tab")
sleep(0.3)
print(">  copy  the 'Location'")
sleep(0.3)
print(" ")
print(" ")
RustShortcut = str(input("> and paste it here : "))
RustShortcut = RustShortcut + "\Rust.lnk"
RustShortcut = r'%s ' %RustShortcut
sleep(2)
print(" ")
print(" ")
print(" ")
print(" file locations stored ")
sleep(1)
print(" ")
print(" ")
print(" ")
print("secondly the program needs the path location of this folder that the program is in:")
sleep(1)
print(" ")
print("this will typically look something like C:\\Downloads")
sleep(1)
print(" ")
print("to find this:")
sleep(1)
print(" ")
print("> find  where  this folder  is located on your computer in windows file explorer")
sleep(0.3)
print("> right click  it")
sleep(0.3)
print(">  click  properties")
sleep(0.3)
print(">  click  'General' tab")
sleep(0.3)
print(">  copy  'Location'")
sleep(0.3)
print(" ")
print(" ")
BatLocation = str(input("> and paste it here : "))
BatLocation = BatLocation + r"\RustAutomated\nonsecureSendKeys.bat"
BatLocation = r'%s ' %BatLocation
print(" ")
print(" ")
print(" ")
print(" file locations stored ")
print(" ")
print(" ")
print(" ")
sleep(1)
print("what local time is wipe for you?")
sleep(0.3)
print("the format is 00:00")
sleep(0.3)
print(" ")
print(" ")

WipeTime = str(input("type the time here : "))

WipeTime = WipeTime.split(":")

WipeHR = int(WipeTime[0])

WipeMIN = int(WipeTime[1])



WipeTime = str(WipeTime[0] + WipeTime[1])

print(" ")
print(" ")

print("your wipe time is: ",WipeTime)

def WhatsTheTime():

    t = time()

    b = str(ctime(t))
    
    c= b.split(" ")
    
    d= c[3].split(":")
    
    e = str(d[0] + d[1])
   
    print("program initiation: ",WipeHR,":",WipeMIN)
    print(" ")
    print("current time:       ",d[0],":",d[1],":",d[2])
    print(" ")

    return e

def process_exists(process_name):

    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    
    output = subprocess.check_output(call).decode()
    
    last_line = output.strip().split('\r\n')[-1]
    
    return last_line.lower().startswith(process_name.lower())

def connect_server():

    keyboard.tap(Key.f1)

    sleep(5)

    keyboard.type("connect 164.132.200.22:28026")
    sleep(10)
    keyboard.tap(Key.enter)

    sleep(5)

    keyboard.tap(Key.f1)

def anti_afk():

    keyboard.press(Key.w)
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

    subprocess.call([BatLocation, "Rust", ""])

    print("rust focused")

while WhatsTheTime() != WipeTime:

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
    
    os.startfile (RustShortcut)
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
