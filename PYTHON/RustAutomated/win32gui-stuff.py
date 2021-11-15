import win32gui
import time
def find_window():
    """find a window by its class_name"""
    _handle = win32gui.FindWindow(None, "RustClient")
    win32gui.SetForegroundWindow(_handle)
    
time.sleep(2)


    


