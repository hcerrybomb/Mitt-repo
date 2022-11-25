import time 
import sys 
import ijson
from simulator.simulator import months

#? THE DAY WITH MOST PASSINGS
#? WHICH HOUR HAS MOST PASSINGS THAT DAY


current_dir = sys.path[0]


date_frequency = set()


with open(f"{current_dir}\\trackdata\\data.json", "rb") as f:
    print("test")
    for data in ijson.items(f, "data"):
        print(len(data))
        for year in range(len(data)):
            for month in range(len(months)):
                for day in range(months[month][1]):
                    for i in range(24):
                        for j in range(3):
                            print(len(data[f"{month}"][f"{day}"][i][j]))
                            date_frequency.add(len(data[f"{month}"][f"{day}"][i][j]))




print(type(date_frequency))
print(date_frequency)