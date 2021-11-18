import time
import os
import pathlib
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


time.sleep(2)
print(style.CYAN + "\nwhat time is wipe for you?"+style.RESET+"\n\ngive your answer in an 00:00 format\n\nexamples:\n\n    17:00\n    15:30\n    04:45\n\n")
time.sleep(1)
UserInput = str(input("give your answer here:   "))
UserInputStatus = False

while UserInputStatus == False:
    if len(UserInput)>5:
        print("\n"+style.RED+"Error:"+style.RESET+" Too many charcters\n\ntry again")
        UserInputStatus = False
        time.sleep(1)
        UserInput = str(input("\ngive your answer here:   "))
    elif UserInput.count(":")<1:
        print(style.RED+"Error:"+style.RESET+" Missing colon\n\ntry again")
        UserInputStatus = False
        time.sleep(1)
        UserInput = str(input("\ngive your answer here:   "))
    elif len(UserInput)<5:
        print(style.RED+"Error:"+style.RESET+" too few characters\n\ntry again")
        UserInputStatus = False
        time.sleep(1)
        UserInput = str(input("\ngive your answer here:   "))
    else:
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        print(style.GREEN+"\n\nwipe time saved succsessfully"+style.RESET)
        UserInputStatus = True
        projFolder = os.path.join(__location__)


        projFolder = r'%s' %projFolder

        print(projFolder)

        WipeTimeInputPath=projFolder+'\WipeTimeInput.txt'

        print(WipeTimeInputPath)

        txtFileRead = open(WipeTimeInputPath, "w")

        txtfilecontent = txtFileRead.write(UserInput)

        txtFileRead.close()


