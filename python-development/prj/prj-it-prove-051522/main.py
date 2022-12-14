import time
import json


#pyreverse -o png -p C:\Users\wista002\Mitt-repo\Mitt-repo\python-development\prj\prj-it-prove-051522\main.py .

#C:\Users\wista002\Mitt-repo\Mitt-repo\python-development\prj\prj-it-prove-051522\main.py

class Album():
    def __init__(
        self,
        artist: str,
        name: str,
        label: str,
        year: int
        ):
        self.artist = artist,
        self.name = name,
        self.label = label,
        self.year = year

    
class Vinyl(Album):
    def __init__(
        self,
        artist,
        name,
        label,
        year,
        color: str,
        rpm: int
        ):
        super().__init__(artist, name, label, year),
        self.color = color
        self.rpm = rpm


class Cd(Album):
    def __init__(
        self,
        artist,
        name,
        label,
        year,
        ):
        super().__init__(artist, name, label, year)


class Collection():
    def __init__(
        self,
        collection_data: list

        ):
        self,
        self.collection_data = collection_data

    def add_record(self, album_obj: dict):
        self.collection_data.append(album_obj)

    def show_albums(self):
        print("albums in collection: ")
        for i in range(len(self.collection_data)):
            album_name = self.collection_data[i]["name"][0]
            print(f"{album_name}")

    def show_artists(self):
        print("artists in collection: ")
        artists_list = []
        for i in range(len(self.collection_data)):
            artist = self.collection_data[i]["artist"][0]
            if artists_list.count(artist) < 1:
                artists_list.append(artist)
            
        for j in range(len(artists_list)):
            print(artists_list[j])


    def show_artist_albums(self,artist_para: str):
        print(f"albums from {artist_para} in collection:")
        for i in range(len(self.collection_data)):
            if self.collection_data[i]["artist"][0] == artist_para:
                album_name = self.collection_data[i]["name"][0]
                print(f"{album_name}")

#? finner current mappe
current_dir = current_dir = __file__[:len(__file__) - len("main.py")]

#? Laster eksempel dataen
with open(current_dir + "example_data.json","r") as file:
    example_data = json.load(file)

collection_data = []
#? lager kolleksjonen
collection = Collection(collection_data)


#? registrerer nye artister og album fra eksempel data
for i in range(len(example_data["data"])):
    if example_data["data"][i]["type"] == "LP":
        vinyl = Vinyl(
            example_data["data"][i]["artist"],
            example_data["data"][i]["album"],
            example_data["data"][i]["label"],
            example_data["data"][i]["year"],
            example_data["data"][i]["color"],
            example_data["data"][i]["rpm"]
        )
        collection.add_record(vinyl.__dict__)
    else: 
        cd = Cd(
            example_data["data"][i]["artist"],
            example_data["data"][i]["album"],
            example_data["data"][i]["label"],
            example_data["data"][i]["year"]
        )
        collection.add_record(cd.__dict__)


print("\n\n")
#? Viser en oversikt over alle platene i samlingen
collection.show_albums()


print("\n\n")
#? Viser en oversikt over alle artistene i samlingen
collection.show_artists()


print("\n\n")
#? viser en oversikt over alle albumene til en gitt artist
collection.show_artist_albums("Taylor Swift")

