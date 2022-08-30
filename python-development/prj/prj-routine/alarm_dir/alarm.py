#PLAYS RANDOM SONG FROM MP3 FOLDER RIGHT AS SCRIPT RUNS
from tracemalloc import start
from dotenv import load_dotenv
import  vlc
import time
from mutagen.mp3 import MP3
import subprocess
import random
import os
from pathlib import Path
import sys
import math as m




#ties it all in a bundle and runs it
def run():
    path = sys.path[0] + '\env-files\.env'
    load_dotenv(path)

    global song_folder
    song_folder = os.getenv("SONG_FOLDER")

    global songs_list
    songs_list = os.listdir(song_folder)    
    if os.getenv('HAS_VOICEMEETER'):
        while getProcessStatus('voicemeeterpro.exe') == False:
            time.sleep(5)
            print("voicemeeter not yet started, waiting")
    start_alarm()

#function for picking a song, once picked its removed from songs_list (on each run)
def pick_song():
    pick_number = random.randint(0,len(songs_list))
    song_path = f'{song_folder}\{songs_list[pick_number]}'
    print(f'{songs_list[pick_number]} picked!')
    songs_list.pop(pick_number)
    return song_path


# function for checking if a process exists, arg is the full process name.exe, in this case voicemeeter
def getProcessStatus(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())

#function for starting the actual alarm, 3sec sleep for voicemeeter (if present in env file), 
#picks song and plays then plays again till list empty
def start_alarm():
    while len(songs_list) != 0:
        time.sleep(3)
        song_path_final = pick_song()
        audio = MP3(song_path_final)
        audio_info = audio.info
        length_in_secs = int(audio_info.length)
        length_minutes = m.floor(length_in_secs/60)
        length_spare_secs = length_minutes * 60 - length_in_secs
        p = vlc.MediaPlayer(song_path_final)
        print(f'playing now, duration: {length_minutes}mins and {length_spare_secs}secs (somethings wrong)')
        p.play()
        time.sleep(length_in_secs)
        p.stop()
        print('song over!\n\n')



#for testing the actual script
if __name__ == "__main__":
    run()
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