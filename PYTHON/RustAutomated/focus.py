import win32gui
import time
import sys

varProgramToFind = "Microsoft Teams"
  
def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

appwindows = get_app_list()

numberOfPrograms = len(appwindows)

for x in range(0,numberOfPrograms):

    if varProgramToFind in str(appwindows[x]):
        print("program nr.",x,":",appwindows[x],"  match")
        correctProgram = str(appwindows[x])
    else:
        print("program nr.",x,":",appwindows[x]," no match")

correctProgram = correctProgram.split("'")
correctProgram = correctProgram[1]
print(correctProgram)
handle = win32gui.FindWindow(None, correctProgram)  
if x==x:
    try:
        win32gui.BringWindowToTop(handle)  
        win32gui.SetForegroundWindow(handle)
        win32gui.SetFocus(handle)
    except:
        print(sys.exc_info()[0], "occurred.")
print("program continuing")

classofhandle = win32gui.GetClassName(handle)




