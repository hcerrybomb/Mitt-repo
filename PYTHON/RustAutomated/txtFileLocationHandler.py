######      IMPORTS

import time
import os
import pathlib

######      COLOR STYLINGS

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

######      VARIABLE DECLARATIONS

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

        projFolder = os.path.join(__location__)                     #projFolder is declared as this projs folder

        projFolder = r'%s' %projFolder                              #projfolder is made into raw string  

        WipeTimeInputPath=projFolder+'\WipeTimeInput.txt'           #wipetimeuserinput is full path of txt file

        txtFileWrite = open(WipeTimeInputPath, "w")                 #opens txt file in write mode

        txtFileWrite.write(UserInput)              #txtfilecontent is re-written as the users VALID input



        txtFileWrite.close()                                        #txtfileclosed


