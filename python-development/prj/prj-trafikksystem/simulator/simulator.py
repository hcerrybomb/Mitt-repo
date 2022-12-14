"""simulator.py can be used both as a standalone script to simulate
car passings with randomly generated car objects and their data sent to
data.json
OR
be used as a module in main.py, also simulating car passings and
sending their data to data.json"""

from atexit import register
import json
import random
import time
import itertools
import threading
import time
import sys
import os
import tracemalloc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
    Simple function that asks the user if they would like to see help
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
            valid = True

        else:
            print("\nInvalid input!")


class SimBil(RegBil):
    """
    Class for car object tracked for the simulator, inherited from
    RegBil class in fillregister.py

    <time_added> string of the hour the car passed the registration
    point.
    """

    def __init__(
        self,
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
    """
    Class for the simulator that simulates an amount of cars
    passing by the registering point and tracking their data
    and moving that data to a .json folder in the local directory.

    <min> the minimum amount of cars that pass each HOUR
    of the simulation.

    <max> the maximum amount of cars that pass each HOUR
    of the simulation.

    <years> is the amount of years the simulation will simulate.

    <target_file> is a string of the file path for the json data file.

    <source_file> is a string of the file path for the register of
    cars made in the fillregister.py script.
    """

    def __init__(
        self,
        target_file: str,
        source_file: str,
        min: int=10,
        max: int=100,
        years: int=1,
        data: dict={"data":{}},
        car_count: int=0,
        sim_start: float=time.time()
        ):

        self.min = min
        self.max = max
        self.years = years
        self.target_file = target_file,
        self.source_file = source_file
        self.data = data
        self.car_count = car_count
        self.sim_start = sim_start

    def simulate(self):
        """
        Method that simulates cars passing by a registering point,
        using the register as example cars and tracking tracking X
        amount of cars per hour, for X amount of years.
        
        The "simulating" is going through each hour and picking a
        random amount of cars to pass that hour, with higher chances
        of more cars passing during rush hours (7-9 and 15-17)
        """
        print('\n')
        dict_start = time.time()

        with open(self.source_file, 'r') as register_file:
            print(f'\rLoading register...',end=' ')
            register = register_file.read()
            register = json.loads(register)
            register = register["register"]
            
        hour_count = 0

        tracemalloc.start()

        len_elec = len(register["electric"]) - 1
        len_foss = len(register["gas"]) - 1
        
        
        for year in range(2022, self.years + 2022):
            self.data["data"].update(
                {f"{year}":{}}
            )

            for month in range(len(MONTHS)): 
                self.data["data"][f"{year}"].update(
                    {f"{MONTHS[month][0]}":[]}
                )
                
                for day in range(MONTHS[month][1]):
                    day_total = 0
                    self.data["data"][f"{year}"][
                    f"{MONTHS[month][0]}"].append(
                        {f"{day}":[]}
                    )

                    for hour in range(24):
                        hour_total = 0
                        self.data["data"][f"{year}"][
                        f"{MONTHS[month][0]}"][
                        day][f"{day}"].append(
                            {f"{hour}":[]}
                        )
                        max = self.max / 2

                        if 10 > hour > 6 or 19 > hour > 14:
                            max = self.max

                        for cars in range(random.randint(self.min, max)):
                            hour_total += 1
                            self.car_count += 1

                            if random.randint(0,1)%2==0:
                                proxCar = register["electric"][
                                random.randint(0,len_elec)]

                            else:
                                proxCar = register["gas"][
                                random.randint(0,len_foss)]

                            self.data["data"][f"{year}"][
                            f"{MONTHS[month][0]}"][day][f"{day}"][hour][
                            f"{hour}"].append(
                                SimBil(
                                    proxCar["id"],
                                    proxCar["brand"],
                                    proxCar["model"],
                                    proxCar["owner"],
                                    proxCar["fuel"],
                                    f"{hour}:00").__dict__
                            )

                        hour_count += 1

                        print(f"\rSimulating drives, "
                        + f" {hour_count}/{self.years * 8760} hours, "
                        + f"{year-2021}/{self.years} year/s ", end=' '
                        )
                        
                        self.data["data"][f"{year}"][
                        f"{MONTHS[month][0]}"][day][f"{day}"][
                        hour][f"{hour}"].append(
                            {"total":hour_total}
                        )
                        day_total += hour_total
                    
                    self.data["data"][f"{year}"][f"{MONTHS[month][0]}"][
                    day].update(
                        {"total":day_total}
                    )
                  
        print(
            f'\rSimulation done.      Elapsed time:   '
            + f'{round(time.time() - dict_start,2)}s     '
            + f'                                       \n'
        )
        del register
    
    def dump_json(self):
        load_start = time.time()
        dumped = False
        
        def loading_str():

            for x in itertools.cycle(["   ",".  ",".. ","..."]):

                if dumped:
                    break
                
                sys.stdout.write(
                    f'\rloading data object to data.txt{x}'
                )
                sys.stdout.flush()
                time.sleep(0.2)

        load_str = threading.Thread(target=loading_str)
        load_str.start()

        with open(self.target_file[0], 'w') as file:
            file.write(json.dumps(self.data, indent=2))
        del self.data
        dumped = True
            
        print(
            f"\rLoaded to txt.        Elapsed time:   "
            + f"{round(time.time() - load_start,2)}s"
            + "                "
        )
        print(
            f'\nSimulation created.   Total time:     '
            + f'{round(time.time() - self.sim_start,2)}s\n'
        )

see_help_sim()

if __name__ == "__main__":
    current_dir = __file__[:len(__file__) - len("simulator.py")]
    source_file_path = current_dir[:len(current_dir) - len("simulator/")]
    source_file_path += "register/register.txt"
    simulator = Simulator(
        target_file = current_dir + "\\data.txt",
        source_file = source_file_path
    )

    simulator.simulate()
    simulator.dump_json()