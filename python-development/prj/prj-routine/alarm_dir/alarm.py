#PLAYS RANDOM SONG FROM MP3 FOLDER RIGHT AS SCRIPT RUNS
from tracemalloc import start
from dotenv import load_dotenv
import vlc
import time
from mutagen.mp3 import MP3
import subprocess
import random
import os
from pathlib import Path
import sys
import math as m
if __name__ == "__main__":
    current_dir = sys.path[0]
    
else:
    current_dir = sys.path[0] + '\\alarm_dir'



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


#ties it all in a bundle and runs it
def run():
    global song_folder
    song_folder = current_dir + '\songs'
    print(song_folder)

    global songs_list
    songs_list = os.listdir(song_folder)   
    print(songs_list) 


    if getProcessStatus('voicemeeterpro.exe') == False:
        print("starting voicemeeter")
        os.startfile("C:\\Program Files (x86)\\VB\\Voicemeeter\\voicemeeterpro.exe")
        time.sleep(5)
        if getProcessStatus('voicemeeterpro.exe') == False:
            print("voicemeeter failed to open, trying again")
            while getProcessStatus('voicemeeterpro.exe') == False:
                print("starting voicemeeter again")
                os.startfile("C:\Program Files (x86)\VB\Voicemeeter\voicemeeterpro.exe")
        start_alarm()
    else:
        print("voicemeeter already open")
        time.sleep(3)
        start_alarm()


#function for picking a song, once picked its removed from songs_list (on each run)
#c:\Users\Gaming_Dator_VII\Desktop\Mitt-repo\python-development\prj\prj-routine\env\.venv-routine\Scripts\python.exe c:\Users\Gaming_Dator_VII\Desktop\Mitt-repo\python-development\prj\prj-routine\alarm_dir\alarm.py
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
def start_alarm():
    print("\n\n\n")
    while len(songs_list) != 0:
        time.sleep(3)
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
            time.sleep(1)
            progress(i+1, length_in_secs, song=song_name)
        p.stop()
        print('\033[00;37msong over!\n\n')



#for testing the actual script
#https://stackoverflow.com/questions/26286660/how-to-make-a-window-fullscreen-in-a-secondary-display-with-tkinter
if __name__ == "__main__":
    run()





























if False:
    username = 'aajk5e9txobgt5mvxqrnj7ctj'
    clientID = '935ddcfe196e4aafadf1d94405d23506'
    clientSecret = '92211f2cd4af461bb42cedfe18f301d8'
    redirectURI = 'http://google.com/'

    oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)

    user = spotifyObject.current_user()
    print(json.dumps(user,sort_keys=True, indent=4))

    search_song = "GET LOST"
    results = spotifyObject.search(search_song, 1, 0, "track")
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)
    print('Song has opened in your browser.')