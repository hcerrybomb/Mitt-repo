#PLAYS RANDOM SONG FROM MP3 FOLDER RIGHT AS SCRIPT RUNS

import  vlc
import time
from mutagen.mp3 import MP3
import subprocess
import random
import os


song_folder = "C:\\Users\\Gaming_Dator_VII\\Desktop\\Mitt-repo\\python-development\\prj-routine\\alarm python venv\\songs"
dir_list = os.listdir(song_folder)

def pick_song():


    pick_number = random.randint(0,len(dir_list))
    song_path = f'C:\\Users\\Gaming_Dator_VII\\Desktop\\Mitt-repo\\python-development\\prj-routine\\alarm python venv\\songs\\{dir_list[pick_number]}'
    dir_list.pop(pick_number)
    return song_path

# function for checking if a process exists, arg is the full process name.exe
def getProcessStatus(process_name):

    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name

    output = subprocess.check_output(call).decode()

    last_line = output.strip().split('\r\n')[-1]

    return last_line.lower().startswith(process_name.lower())


while getProcessStatus('voicemeeterpro.exe') == False:
    time.sleep(5)
    print("voicemeeter not yet started, waiting")
else:
    while len(dir_list) != 0:
        time.sleep(3)
        print("voicemeeter started, playing mp3")
        song_path_final = pick_song()
        audio = MP3(song_path_final)
        audio_info = audio.info
        length_in_secs = int(audio_info.length)


        p = vlc.MediaPlayer(song_path_final)

        print(f"playing song: {song_path_final}")
        p.play()
        time.sleep(length_in_secs)
        print(f"duration {length_in_secs}")
        p.stop()
        print("song over")






























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