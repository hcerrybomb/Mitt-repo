import json
import datetime
import string
import random
import time
import sys
import csv
import names
import json

def see_help_ask():
    """
    Simple function that asks the user if they would like to see help for the classes-
    of fillregister.py
    """
    valid = False
    while valid == False:
        seeHelp = str(input("See help for fillregister.py? [y/n] : " ))
        if seeHelp == "y" or seeHelp == "Y":
            help(regBil)
            help(register)
            valid = True
        elif seeHelp == "n" or seeHelp == "N":
            print("Continuing program")
            valid = True
        else:
            print("Invalid input")


def gen_number_plate():
    """
    Function for generating number plate strings, simply returns a string-
    of 2 letters and 5 numbers at random.
    """

    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = random.randint(10000, 100000)
    return f'{letters}-{numbers}'


class regBil:
    """
    Class for car objects that are sent to the register of cars.
    <id> is the number plate, <fuel> is either "electric", "gasoline", or "diesel".
    Rest are pretty self explanatory.
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
        """
        Prints f string of all variables of object.
        """

        print(f"\n\nPlate:{self.id}\nBrand:{self.brand}\nModel:{self.model}\nOwner:{self.owner}\nFuel/El:{self.fuel}")


class register():
    """
    Class for instantiating the register of cars to be used in the simulator.
    <targetFile> is the target path for the .json file that will become the register of cars.
    <sourceFile> is the source path for the .csv models file filled with car models.
    """

    def __init__(
        self,
        targetFile:str,
        sourceFile:str
    ):
        self.targetFile = targetFile
        self.sourceFile = sourceFile
    
    def fillRegister(self,amt:int=1000):
        """
        Function that makes a python dict object filled with randomized car objects-
        that are sent to the .json register. 
        <amt> is the amount of car objects to be created and sent to the register.
        """

        models = []
        fuels = ['electric','gasoline','diesel']
        with open(self.targetFile, 'w') as file:
            json.dump({"register":[]}, file)
        with open(self.sourceFile, "r") as models:
            csvreader = csv.reader(models)
            header = next(csvreader)
            models=[]
            for row in csvreader:
                models.append([row[1], row[2]+" "+row[0],fuels[random.randint(0,2)]])
        with open(self.targetFile, 'r') as file:
            data = json.load(file)
        with open(self.targetFile, 'w') as file:
            for i in range(amt):
                build = models[random.randint(0,len(models)-1)]
                car = regBil(gen_number_plate(),build[0],build[1],names.get_full_name(),build[2])
                data['register'].append(car.__dict__)
            json.dump(data, file, indent=4)


see_help_ask()
if __name__ == "__main__":
    current_dir = sys.path[0]
    reg = register(
        targetFile=current_dir + "\\test.json", # * you can test the program in test.json
                                                # * register.json is already filled with 
                                                # * 100k objects, apprx 5 min run time
        sourceFile=current_dir + "\\models.csv",
    )
    reg.fillRegister(1000)