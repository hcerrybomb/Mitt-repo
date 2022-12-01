import json
import random
import time
import itertools
import threading
import time
import sys
import tracemalloc
import path
folder = path.Path(__file__).abspath()
sys.path.append(folder.parent.parent.parent)
from register.fillregister import RegBil
months = [
    ["Jan",31],
    ["Feb",28],
    ["Mar",31],
    ["Apr",30],
    ["May",31],
    ["Jun",30],
    ["Jul",31],
    ["Aug",31],
    ["Sep",30],
    ["Oct",31],
    ["Nov",30],
    ["Dec",31]
]


def see_help_sim():
    """
    Simple function that asks the user if they would like to see help for the classes-
    of simulator.py
    """
    valid = False
    while valid == False:
        seeHelp = str(input("\nSee help for simulator.py? [y/n] : " ))
        if seeHelp == "y" or seeHelp == "Y":
            help(SimBil)
            help(Simulator)
            valid = True
        elif seeHelp == "n" or seeHelp == "N":
            print("\nContinuing program\n\n")
            valid = True
        else:
            print("\nInvalid input")


class SimBil(RegBil):
    """
    class for car object tracked from simulator
    """
    def __init__(self,
                id,
                brand,
                model,
                owner,
                fuel,
                timeAdded:str
    ):
        super().__init__(id,brand,model,owner,fuel)
        self.timeAdded = timeAdded


class Simulator():
    """
    Class for the simulator that simulates an amount of cars passing by-
    the registering point and tracking their data and moving that data-
    to a .json folder in the local directory.

    <min> is the minimum amount of cars that pass each HOUR of the simulation.
    <max> is the maximum amount of cars that pass each HOUR of the simulation.
    <years> is the amount of years the simulation will simulate.
    <targetFile> is a string of the file path for the json data file.
    <sourceFile> is a string of the file path for the register of cars-
    made in the fillregister.py script.
    """
    def __init__(self,
                min:int,
                max:int,
                years:int,
                targetFile:str,
                sourceFile:str,
    ):

        self.min = 10
        self.max = 100
        self.years = 1
        self.targetFile = targetFile,
        self.sourceFile = sourceFile

    def simulate(self):
        """
        Method that simulates cars passing by a registering point, using the register as-
        example cars and tracking tracking X amount of cars per hour, for X amount of years.
        
        The "simulating" is going through each hour and picking a random amount of cars to-
        pass that hour, with higher chances of more cars passing during rush hours (7-9 and 15-17)
        """
        with open(self.sourceFile, 'r') as registerFile:
            register = json.load(registerFile)
            register = register["register"]
            
        with open(self.targetFile[0], 'w') as dataFile:
            hourCount = 0
            carCount = 0
            start = time.time()
            tracemalloc.start()
            len_elec = len(register["electric"]) - 1
            len_foss = len(register["gas"]) - 1
            data = {"data":{}}
            for year in range(2022, self.years + 2022):
              data["data"].update({f"{year}":{}})
              for month in range(len(months)): #! HERHEHREHREHHRE
                data["data"][f"{year}"].update({f"{months[month][0]}":[]})
                for day in range(months[month][1]):
                  day_total = 0
                  data["data"][f"{year}"][f"{months[month][0]}"].append({f"{day}":[]})
                  for hour in range(24):
                    hour_total = 0
                    data["data"][f"{year}"][f"{months[month][0]}"][day][f"{day}"].append({f"{hour}":[]})
                    max = self.max / 2
                    if 10 > hour > 6 or 19 > hour > 14: max = self.max
                    for cars in range(random.randint(self.min, max)):
                      hour_total += 1
                      carCount += 1
                      if random.randint(0,1)%2==0:proxCar = register["electric"][random.randint(0,len_elec)]
                      else:proxCar = register["gas"][random.randint(0,len_foss)]
                      data["data"][f"{year}"][f"{months[month][0]}"][day][f"{day}"][hour][f"{hour}"].append(
                        SimBil(proxCar["id"],proxCar["brand"],proxCar["model"],proxCar["owner"],proxCar["fuel"],f"{hour}:00").__dict__)
                    hourCount += 1
                    print(f"\rSimulating and adding drives to data: {hourCount}/{self.years * 8760} hours ({self.years}) year/s     memory: {tracemalloc.get_traced_memory()}",end=' ')
                    data["data"][f"{year}"][f"{months[month][0]}"][day][f"{day}"][hour][f"{hour}"].append({"total":hour_total})
                    day_total += hour_total
                  data["data"][f"{year}"][f"{months[month][0]}"][day].update({"total":day_total})
              print(f'\nElapsed time {round(time.time() - start,2)}s\n\n')


            dumped = False
            def loading_str():
                for x in itertools.cycle(["   ",".  ",".. ","..."]):
                    if dumped:
                        break
                    sys.stdout.write(f'\rloading to .json file (usually 1 min) {x}')
                    sys.stdout.flush()
                    time.sleep(0.2)
            load_str = threading.Thread(target=loading_str)
            load_str.start()
            json.dump(data, dataFile, indent=2)
            dumped = True
                
            print(f"\r.json file updated {carCount} total car passings tracked and registered")
            print(f'elapsed time {round(time.time() - start,2)}s\n')


see_help_sim()
if __name__ == "__main__":
    current_dir = sys.path[0]
    simulator = Simulator(
        min = 10,
        max = 100,
        years = 1,
        targetFile = current_dir + "\\data.json",
        sourceFile = current_dir[:len(current_dir)-len("simulator\\test")] + "\\register\\test.json"
    )
    simulator.simulate()