"""main.py is a standalone script that analyses the data from the
simulator and displays the days and hours with the most passings.

This system is built in with the intention of simulating a somewhat
realistic scenario and data usage in mind, which is why the register
and the simulation is of such big scale. While this does add some run
time to the scripts i believe its cooler to have it be a little slower
and more realistic. """
import time 
import sys 
import json
import path

from register.fillregister import Register
from simulator.simulator import Simulator, MONTHS

CURRENT_DIR = sys.path[0]
max_days = []

days_known = False


def see_help_main():
    """
    Simple function that asks the user if they would like to see help
    for the classes in main.py
    """

    valid = False

    while valid == False:
        see_help = str(input("\nSee help for main.py? [y/n] : " ))

        if see_help == "y" or see_help == "Y":
            help(Display)
            valid = True

        elif see_help == "n" or see_help == "N":
            print("\nContinuing program\n\n")
            valid = True

        else:
            print("\nInvalid input")


class Display():
    """
    Class that displays the day(s) that had the most passings past the
    registering point-and the hour(s) that had the most passings in 
    those day(s).

    <source_file> is a string of the file path for the data gathered 
    in the simulation from simulator.py
    """

    def __init__(
        self,
        source_file:str
        ):

        self.source_file = source_file


    def day(self):
        """
        Method that prints the day(s) with the most amount of passings.

        Simply put it takes all the total passings of each day, adds
        that data to a list, and finds the max value and its 
        associated date(s).
        """

        global days_known
        days_known = True

        with open(self.source_file, 'r') as data_file:
            data = json.load(data_file)
            data = data["data"]
            days = []
            days_data = []

            for year in range(len(data)):

                for month in range(len(data[f"{2022+year}"])):

                    for day in range(
                        len(data[f"{2022+year}"][f"{MONTHS[month][0]}"])
                        ):

                        days.append(
                            data[f"{2022+year}"][f"{MONTHS[month][0]}"][
                            day]["total"]
                        )

                        days_data.append({
                            "year":f"{2022+year}",
                            "month":f"{MONTHS[month][0]}",
                            "day":f"{day}"
                        })

            while True:
                max_day_index = days.index(max(days))
                max_day_int = days[max_day_index]
                max_day_data = days_data[max_day_index]

                max_days.append(max_day_data)

                del days[max_day_index]
                del days_data[max_day_index]

                if days[days.index(max(days))] < max_day_int:
                    break

            print(f'\nDagen(e) med flest passeringer var:\n')

            for i in range(len(max_days)):
                print(
                    f'\t{max_days[i]["month"]} {max_days[i]["day"]}. '
                    + f'{max_days[i]["year"]}'
                )

            print(f'\nAntallet var: {max_day_int}\n')
        
    
    def hour(self):
        """
        Method that prints the hour(s) with the most passings for the
        day(s) with the most passings.

        It uses a very similar method to the Display.day() function
        adding the total count of passings for every hour in the day
        a list and finding the max value and its associated hour in 
        that list.
        """

        if days_known == False:
            Display.day()

        with open(self.source_file, 'r') as data_file:
            data = json.load(data_file)
            data = data["data"]
            hours = []
            
            for i in range(0,len(max_days)):
                max_hours = []
                max_day = data[f'{max_days[i]["year"]}'][
                f'{max_days[i]["month"]}'][int(max_days[i]["day"])]
                
                for j in range(24):
                    hour_total = max_day[max_days[i]["day"]][j][
                    f"{j}"][-1]["total"]

                    hours.append(hour_total)
            


                while True:
                    max_hour_index = hours.index(max(hours))
                    max_hour_int = hours[max_hour_index]

                    max_hours.append(max_hour_index)
                    del hours[max_hour_index]

                    if hours[hours.index(max(hours))] < max_hour_int:
                        break
        
                print(
                    f'\nDen {max_days[i]["day"]}. {max_days[i]["month"]}'
                    + f'  {max_days[i]["year"]} var timen(e)'
                    + f' med flest passeringer:\n'
                )
                
                for k in range(len(max_hours)):
                    print(f'\t{max_hours[k]}:00-{max_hours[k]+1}:00')
                
                print(f"\nAntallet var: {max_hour_int}")


if __name__ == "__main__":
    display = Display(
        source_file = CURRENT_DIR + "\\simulator\\data.json"
    )

    register = Register(
        target_file = CURRENT_DIR + "\\register\\register.json",           
        models_file = CURRENT_DIR + "\\register\\resources\\models.csv",
        names_file = CURRENT_DIR + "\\register\\resources\\names.csv",
        amt = 100000
    )

    simulator = Simulator(
        min = 10,
        max = 100,
        years = 1,
        target_file = CURRENT_DIR + "\\simulator\\data.json",
        source_file = CURRENT_DIR + "\\register\\register.json"
    )

    print(
        "The register is already filled and a tracked simulation\n"
        +"has already been run, but you can OPTIONALLY run both\n"
        +"these scripts to test that they work.\n"
        +"By default there is 100'000 different cars/persons in\n"
        +"the register, and the simulation simulates 1 year (8760 hours)\n"
        +"of between 10 and 100 cars passing by each hour."
        )

    valid = False

    while valid == False:
        gen_register = str(input(
            f"\nFill the register with 100000 random cars? [y/n] : "
        ))

        if gen_register == "y" or gen_register == "Y":
            register.fill_register()
            valid = True

        elif gen_register == "n" or gen_register == "N":
            print("\nContinuing program\n\n")
            valid = True

        else:
            print("\nInvalid input")
    
    valid = False

    while valid == False:
        simulate = str(input(
            f"\nSimulate cars passing registering point for "
            + f"({simulator.years}) year(s)? [y/n] : "
        ))

        if simulate == "y" or simulate == "Y":
            simulator.simulate()
            valid = True

        elif simulate == "n" or simulate == "N":
            print("\nContinuing program\n\n")
            valid = True

        else:
            print("\nInvalid input")

    display.day()
    display.hour()

    print("\n\nProgram done.")