import json
import time
import random

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

class Camera:
    


def sendCar():

def simulateCars(yrs:int=1):
    for i in range(yrs):
        for i in range(len(months)):
            for j in range(months[i][1]):
                for k in range(24):
                    print(f"it is now {months[i][0]}, {j+1}. hr:{k}:00 - {k+1}:00")


simulateCars()

if __name__ == "__main__":
    print("done")

# ? for i in range months
# ? for i in range days
# ? for i in range hours 
# ? pass X random int of cars, go t next hour, repeat
