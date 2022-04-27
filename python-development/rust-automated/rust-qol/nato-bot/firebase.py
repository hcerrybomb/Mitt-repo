import interactions
import os
from dotenv import load_dotenv #python-dotenv
from pathlib import Path


import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(Path('C:/Users/Gaming_Dator_VII/Desktop/Mitt-repo/python-development/rust-automated/rust-qol/nato-bot/serviceAccountKey.json'))
firebase_admin.initialize_app(cred)

db = firestore.client()
collection = db.collection("nato-db")

DBdocs = collection.get()

print(DBdocs[0].to_dict())

inp = "W16"

for i in range(len(DBdocs)):
    if inp == DBdocs[i].to_dict()['name']:
        updated_array = DBdocs[i].to_dict()['data'] 
        updated_array.append({
            'playername':"testName",'steamlink':'http://steamcommunity.com/id/test'
            })

        print(updated_array)

