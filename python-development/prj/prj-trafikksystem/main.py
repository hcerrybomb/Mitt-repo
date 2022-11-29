import time 
import sys 
import json
import numpy as np
import path

from register.fillregister import RegBil
from simulator.simulator import months

#? THE DAY WITH MOST PASSINGS
#? WHICH HOUR HAS MOST PASSINGS THAT DAY

current_dir = sys.path[0]

max_days = []
days_known = False

class Display():
    def __init__(
        self,
        sourceFile:str
    ):
        self.sourceFile = sourceFile

    def day(self):
        with open(self.sourceFile, 'r') as dataFile:
            print(self.sourceFile)
            data = json.load(dataFile)
            data = data["data"]
            days = []
            daysData = []
            for year in range(len(data)):
                for month in range(len(data[f"{2022+year}"])):
                    for day in range(len(data[f"{2022+year}"][f"{months[month][0]}"])):
                        days.append(data[f"{2022+year}"][f"{months[month][0]}"][day]["total"])
                        daysData.append({
                            "year":f"{2022+year}",
                            "month":f"{months[month][0]}",
                            "day":f"{day}"
                            })

            max_index = days.index(max(days))
            max_value = days[max_index]
            max_data = daysData[max_index]
            max_days.append(max_data)

            print(f'\nDagen(e) med flest passeringer var:\n')
            for i in range(len(max_days)):
                print(f'{max_days[i]["year"]} {max_days[i]["month"]} {max_days[i]["day"]}. Antallet var: {days[max_index]}')
            print(f'\n\nAntallet var: {max_value}\n')
    
    def hour(self):
        with open(self.sourceFile, 'r') as dataFile:
            print(self.sourceFile)
            data = json.load(dataFile)
            data = data["data"]
            hours = []
            hoursData = []
            for i in range(0,len(max_days)):
                
                max_day = data[f'{max_days[i]["year"]}'][f'{max_days[i]["month"]}'][int(max_days[i]["day"])]
                for i in range(0,23):
                    print("test")
                    print(max_day)

                #print(f'{max_days[i]["year"]} {max_days[i]["month"]} {max_days[i]["day"]}. Antallet var: {days[max_index]}')
            #print(f'\n\nAntallet var: {max_value}\n')

            


display = Display(
    sourceFile = current_dir + "\\simulator\\test\\data.json"
)

display.day()
display.hour()