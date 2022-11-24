import json
import random
import time
import itertools
import threading
import time
import sys
import tracemalloc

sys.path.append('../prj-trafikksystem')
from register.fillregister import regBil

class simBil(regBil):
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


class simBil(regBil):
    """
    HELpppp
    """
    def __init__(
        self, 
        id:str, 
        brand:str, 
        model:str,
        owner:str,
        fuel:str,
        timeAdded:str

        ):

        self.id = id
        self.brand = brand
        self.model = model
        self.owner = owner
        self.fuel = fuel
        self.timeAdded = timeAdded

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

tracemalloc.start()

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\rloading to .json file {c}   memory: {tracemalloc.get_traced_memory()}')
        sys.stdout.flush()
        
        time.sleep(0.1)


current_dir = sys.path[0]

register = f"{current_dir[:len(current_dir) - 10]}\\register\\register.json"

def trackData(min:int=10,max:int=100,years:int=1):
    """
    A function that tracks the data from a simulation of cars passing by a 
    a register point, tracking the data of each car and moving it to a .json
    file. <min> var is the minimum amount of cars passing each hour, <max> is the 
    maximum of the same, <years> is how many years the simluation will last.  
    """
    t = threading.Thread(target=animate)
    start = time.time()
    with open(f"{current_dir[:len(current_dir) - 10]}\\register\\register.json", 'r') as file1:
        register = json.load(file1)
        register = register["register"]

    with open(f"{current_dir}\\data.json", 'w') as file2:
        
        count = 0
        count2 = 0
        
        data = {"data":{}}
        print('\n')
        for i in range(2022, years + 2022):
            new = {f"{i}":{}}
            data["data"].update(new)
            for j in range(len(months)):
                new = {f"{months[j][0]}":{}}
                data["data"][f"{i}"].update(new)
                for k in range(1,months[j][1]+1):
                    new = {f"{k}":{}}
                    data["data"][f"{i}"][f"{months[j][0]}"].update(new)
                    for l in range(24):
                        new = {f"{l}:00":{
                            "electric":[],
                            "fossil":[]
                        }}
                        data["data"][f"{i}"][f"{months[j][0]}"][f"{k}"].update(new)
                        for m in range(random.randint(min,max)):
                            count2 += 1
                            index = random.randint(0,99999)


                            proxCar = register[index]


                            fuelVar = "fossil"
                            if proxCar["fuel"]=="electric":
                                fuelVar = "electric"


                            new = simBil(proxCar["id"],proxCar["brand"],proxCar["model"],proxCar["owner"],proxCar["fuel"],f"{l}:00")
                            data["data"][f"{i}"][f"{months[j][0]}"][f"{k}"][f"{l}:00"][fuelVar].append(new.__dict__)
                        count+=1

                        print(f"\rSimulating and adding drives to data: {count}/8760 hours ({years}) year/s     memory: {tracemalloc.get_traced_memory()}",end=' ')
            print(f'\nelapsed time {round(time.time() - start,2)}s\n')
            print(f"")
            t.start()


            json.dump(data,file2,indent=2)
            
            done = True
            print(f"\r.json file updated {count2} total car passings tracked and registered")
            print(f'elapsed time {round(time.time() - start,2)}s\n')

if __name__ == "__main__":
    help(trackData)
    done = True
        
