import datetime
import time
import tkinter as tk
from tracemalloc import start
from dotenv import load_dotenv
import vlc
from mutagen.mp3 import MP3
import subprocess
import random
import os
from pathlib import Path
import sys
import math as m
import asyncio





#gets current work dir
current_dir = sys.path[0]

#progress bar yoinked from the internet
def progress(count, total, song=''):
    red='\033[01;31m'
    gre='\033[02;32m'
    yel='\033[00;33m'
    blu='\033[01;34m'

    
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    
    percentage = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    secs_done = count
    mins_done = count // 60
    spare_secs_done = secs_done % 60

    secs = total
    mins = secs // 60
    spare_secs = secs % 60
    
    
    if percentage <= 50:
        col = red
    elif percentage > 50 and percentage <= 80:
        col = yel
    elif percentage > 80 and percentage <= 99:
        col = gre
    else:
        col = blu
    
    sys.stdout.write('\r{0} {1}:{2} {3} {4}:{5}  {6}'.format(col, mins_done, spare_secs_done, bar, mins, spare_secs, song))
    
    sys.stdout.flush()


#function for picking a song, once picked its removed from songs_list (on each run)
def pick_song():
    pick_number = random.randint(0,len(songs_list)-1)
    song_path = f'{song_folder}\{songs_list[pick_number]}'
    print(f'{songs_list[pick_number]} picked!')
    
    song_name = songs_list[pick_number]
    song_name = song_name[:-4]
    songs_list.pop(pick_number)
    return (song_path, song_name)


# function for checking if a process exists, arg is the full process name.exe, in this case voicemeeter
def getProcessStatus(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


#function for starting the actual alarm, 3sec sleep for voicemeeter (if present in env file), 
#picks song and plays then plays again till list empty
async def start_alarm():
    print("\n\n\n")
    while len(songs_list) != 0:
        await asyncio.sleep(3)
        song_path_final, song_name = pick_song()
        audio = MP3(song_path_final)
        audio_info = audio.info
        length_in_secs = int(audio_info.length)
        length_minutes = length_in_secs // 60
        length_spare_secs = length_in_secs % 60
        p = vlc.MediaPlayer(song_path_final)
        print(f'playing now') 
        
        print(f'duration: {length_minutes}mins and {length_spare_secs}secs')
        p.play()
        for i in range(length_in_secs): 
            await asyncio.sleep(1)
            progress(i+1, length_in_secs, song=song_name)
        p.stop()
        print('\033[00;37msong over!\n\n')

#ties it all in a bundle and runs it
async def run_alarm():
    global song_folder
    song_folder = current_dir + '\songs'
    print(song_folder)

    global songs_list
    songs_list = os.listdir(song_folder)   
    print(songs_list) 
    if os.getenv('HAS_VOICEMEETER') == "True":
        while getProcessStatus('voicemeeterpro.exe') == False:
            await asyncio.sleep(5)
            print("voicemeeter not yet started, waiting")
    await start_alarm()


#inits some essential vars
today = datetime.date.today()
weekday = datetime.datetime.today().weekday()
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

friday_bus = ["Friday",7,34] if datetime.date.today().isocalendar()[1] % 2 == 0 else ["Friday",9, 19]

cases = [
    ["Monday",      7, 34],
    ["Tuesday",     9, 19],
    ["Wednesday",   9, 19],
    ["Thursday",    7, 34],
    friday_bus,
    ["Saturday",    23, 30],
    ["Sunday",      12, 10],
]

#makes the text for the tkinter gui
def make_text():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    secs_till = 60 - int(current_time[6:8])

    hrs_till = cases[weekday][1] - int(current_time[0:2])

    print(hrs_till)

    if hrs_till < 0:
        hrs_till = 0
        mins_till = 0
        secs_till = 0
    else: 

        if cases[weekday][2] > int(current_time[3:5]): 
            mins_till = cases[weekday][2] - int(current_time[3:5]) - 1
        else:
            if hrs_till != 0: 
                hrs_till -= 1
                mins_till = 60 - int(current_time[3:5]) + cases[weekday][2] - 1
            else:
                mins_till = 0
                secs_till = 0

    made_text = f"It is {cases[weekday][0]}, {today}, {current_time} \nbus leaves in {hrs_till}hrs {mins_till}mins {secs_till}secs"
    l.config(text=made_text, fg="red")
    root.after(1000, make_text)

#some more vars
root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())

l = tk.Label(text='', font=("Helvetica", 60))
l.pack(expand=True)

#ties it all together and runs for BUS
async def run_bus():
    make_text()
    try:
        root.mainloop()
        print("running")
    except TypeError:
        print("TypeError, continuing")
        

#syncs the courotines to run at same time
async def asyncmain():
    task1 = asyncio.create_task(
        run_bus()
    )
    task2 = asyncio.create_task(
        run_alarm()
    )
    await task1
    await task2


#main 
def main():
    asyncio.run(asyncmain())

if __name__ == "__main__":
    main()
