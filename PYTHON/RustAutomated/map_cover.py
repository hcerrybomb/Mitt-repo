from pynput.keyboard import Listener, Key, Controller
import time
#TrueOrFalse = "RustClient.exe" in (i.name() for i in psutil.process_iter())
keyboard = Controller()

def on_press(key):
    text = '{0} pressed'.format(
        key)

def on_release(key):
    KeyPressedText = '{0} pressed'.format(
        key)
    KeyPressedText = str(KeyPressedText)
    print(str(KeyPressedText))
    KeyText = "Key"
    if KeyText in KeyPressedText:
        return
    else:
        if key.char == 'g':
            time.sleep(0.05)
            keyboard.press(Key.scroll_lock)
            time.sleep(0.05)
            keyboard.release(Key.scroll_lock)

            
            
            
            


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

        
