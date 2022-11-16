import json
import datetime
import string
import random
import time
import sys
import csv
import names
import json


class regBil:
    """
    HELpppp
    """
    def __init__(
        self, 
        id:str, 
        brand:str, 
        model:str,
        owner:str,
        fuel:str
        ):

        self.id = id
        self.brand = brand
        self.model = model
        self.owner = owner
        self.fuel = fuel
    def pPrintInfo(self):
        print(f"\n\nPlate:{self.id}\nBrand:{self.brand}\nModel:{self.model}\nOwner:{self.owner}\nFuel/El:{self.fuel}")
    def passerPunkt():
        


current_dir = sys.path[0]


modelsPath = current_dir + "\\models.csv"
models = []
fuels = ['electric','gasoline','diesel']

jsonPath = current_dir + "\\register.json"
with open(jsonPath, 'w') as file:
    json.dump({"register":[]}, file)

with open(modelsPath, "r") as models:
    csvreader = csv.reader(models)
    header = next(csvreader)
    models=[]
    for row in csvreader:
        models.append([row[1], row[2]+" "+row[0],fuels[random.randint(0,2)]])



def gen_number_plate():
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = random.randint(10000, 100000)
    return f'{letters}-{numbers}'


def fillRegister(amt:int):
    with open(jsonPath, 'r') as file:
        data = json.load(file)
    with open(jsonPath, 'w') as file:
        for i in range(amt):
            build = models[random.randint(0,len(models)-1)]
            car = regBil(gen_number_plate(),build[0],build[1],names.get_full_name(),build[2])
            data['register'].append(car.__dict__)

        json.dump(data, file, indent=4)
        

start = time.time()
fillRegister(100000)
end = time.time()
print(f"executoin time:{end - start}")



    #? function printData(start, end):
    #? list off registers with unix time in object
    #? start = xxxx unix time, end = xxxxx unix time
    #? in function convert unix to date for pretty
    #? find start:
    #? middle, middle, middle, bubble sort or whatever
    #? find start
    #? while end>unix time, go to next object
    #? send object to main, make table or stats or whatever, show peak times and whatevs
    #? if no start,end given then do all time / total
