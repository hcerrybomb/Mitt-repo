import win32gui
import time
def find_window():
    """find a window by its class_name"""
    _handle = win32gui.FindWindow(None, "RustClient")
    win32gui.SetForegroundWindow(_handle)
    
time.sleep(2)



def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print (hex(hwnd), win32gui.GetWindowText( hwnd ))

#win32gui.EnumWindows( winEnumHandler, None )

import win32gui
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
for i in appwindows:
    print(i)

handle = win32gui.FindWindow(None, "win32gui__GetClassName_meth.html - Google Chrome")  
win32gui.BringWindowToTop(handle)  
win32gui.SetForegroundWindow(handle)
classofhandle = win32gui.GetClassName(handle)
print(classofhandle)
#win32gui.SetFocus(handle)


