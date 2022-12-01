"""simulator.py can be used as both a standalone script to use """
import json
import random
import time
import itertools
import threading
import time
import sys
import tracemalloc
import path



FOLDER = path.Path(__file__).abspath()
sys.path.append(FOLDER.parent.parent)

from register.fillregister import RegBil


MONTHS = [
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
    Simple function that asks the user if they would like to see help-
    for the classes of simulator.py
    """
    valid = False

    while valid == False:
        see_help = str(input("\nSee help for simulator.py? [y/n] : " ))

        if see_help == "y" or see_help == "Y":
            help(SimBil)
            help(Simulator)
            valid = True

        elif see_help == "n" or see_help == "N":
            print("\nContinuing program\n\n")
            valid = True

        else:
            print("\nInvalid input")


class SimBil(RegBil):
    """
    Class for car object tracked for the simulator, inherited from-
    RegBil class in fillregister.py

    <time_added> 
    """

    def __init__(self,
                id,
                brand,
                model,
                owner,
                fuel,
                time_added: str
                ):
        
        super().__init__(id, brand, model, owner, fuel)
        self.time_added = time_added


class Simulator():
    """Class for the simulator that simulates an amount of cars- 
    passing by the registering point and tracking their data-
    and moving that data to a .json folder in the local directory.

    <min> the minimum amount of cars that pass each HOUR- 
    of the simulation.

    <max> the maximum amount of cars that pass each HOUR- 
    of the simulation.

    <years> is the amount of years the simulation will simulate.

    <target_file> is a string of the file path for the json data file.

    <source_file> is a string of the file path for the register of- 
    cars made in the fillregister.py script."""

    def __init__(self,
                min: int,
                max: int,
                years: int,
                target_file: str,
                source_file: str,
                ):

        self.min = 10
        self.max = 100
        self.years = 1
        self.target_file = target_file,
        self.source_file = source_file

    def simulate(self):
        """Method that simulates cars passing by a registering point,
        using the register as example cars and tracking tracking X-
        amount of cars per hour, for X amount of years.
        
        The "simulating" is going through each hour and picking a- 
        random amount of cars to pass that hour, with higher chances- 
        of more cars passing during rush hours (7-9 and 15-17)"""

        with open(self.source_file, 'r') as register_file:
            register = json.load(register_file)
            register = register["register"]
            
        with open(self.target_file[0], 'w') as data_file:
            hour_count = 0
            car_count = 0

            start = time.time()
            tracemalloc.start()

            len_elec = len(register["electric"]) - 1
            len_foss = len(register["gas"]) - 1

            data = {"data":{}}
            
            for year in range(2022, self.years + 2022):
                data["data"].update(
                    {f"{year}":{}}
                    )

                for month in range(len(MONTHS)): 
                    data["data"][f"{year}"].update(
                        {f"{MONTHS[month][0]}":[]}
                        )
                    
                    for day in range(MONTHS[month][1]):
                        day_total = 0
                        data["data"][f"{year}"][f"{MONTHS[month][0]}"].append(
                            {f"{day}":[]}
                            )

                        for hour in range(24):
                            hour_total = 0
                            data["data"][f"{year}"][f"{MONTHS[month][0]}"][
                            day][f"{day}"].append(
                                {f"{hour}":[]}
                                )

                            max = self.max / 2

                            if 10 > hour > 6 or 19 > hour > 14:
                                 max = self.max

                            for cars in range(random.randint(self.min, max)):
                                hour_total += 1
                                car_count += 1

                                if random.randint(0,1)%2==0:
                                    proxCar = register["electric"][
                                        random.randint(0,len_elec)]

                                else:
                                    proxCar = register["gas"][
                                        random.randint(0,len_foss)]

                                data["data"][f"{year}"][f"{MONTHS[month][0]}"][
                                    day][f"{day}"][hour][f"{hour}"].append(
                                    SimBil(
                                        proxCar["id"],
                                        proxCar["brand"],
                                        proxCar["model"],
                                        proxCar["owner"],
                                        proxCar["fuel"],
                                        f"{hour}:00").__dict__
                                    )

                            hour_count += 1

                            print(f"\rSimulating and adding drives to data:"+
                            f" {hour_count}/{self.years * 8760} hours "+
                            f"({self.years}) year/s    memory: "+
                            f"{tracemalloc.get_traced_memory()}",end=' ')
                            
                            data["data"][f"{year}"][f"{MONTHS[month][0]}"][
                                day][f"{day}"][hour][f"{hour}"].append(
                                    {"total":hour_total}
                                    )
                            
                            day_total += hour_total
                        
                        data["data"][f"{year}"][f"{MONTHS[month][0]}"][
                            day].update(
                                {"total":day_total}
                                )
                
                print(f'\nElapsed time {round(time.time() - start,2)}s\n\n')
            
            dumped = False
            
            def loading_str():
                for x in itertools.cycle(["   ",".  ",".. ","..."]):

                    if dumped:
                        break
                    
                    sys.stdout.write(
                        f'\rloading to .json file (usually 1 min) {x}')
                    sys.stdout.flush()
                    time.sleep(0.2)

            load_str = threading.Thread(target=loading_str)
            load_str.start()

            json.dump(data, data_file, indent=2)

            dumped = True
                
            print(f"\r.json file updated {car_count}"+
            f" total car passings tracked and registered")
            print(f'elapsed time {round(time.time() - start,2)}s\n')


see_help_sim()

if __name__ == "__main__":
    current_dir = sys.path[0]

    simulator = Simulator(
        min = 10,
        max = 100,
        years = 1,
        target_file = current_dir + "\\data.json",
        source_file = current_dir[:len(current_dir)-len("simulator")] + 
        "register\\register.json"
    )

    simulator.simulate()