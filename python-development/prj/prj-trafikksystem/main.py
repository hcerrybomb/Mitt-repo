"""main.py is a standalone script that analyses the data from the
simulator and displays the days and hours with the most passings.

This system is built in with the intention of simulating a somewhat
realistic scenario and data usage in mind, which is why the register
and the simulation is of such big scale. While this does add some run
time to the scripts i believe its cooler to have it be a little slower
and more realistic. """
from calendar import day_abbr
import time 
import sys 
import json
import path

from register.fillregister import Register
from simulator.simulator import Simulator, MONTHS

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
            valid = True

        else:
            print("\nInvalid input!")


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
        source_file: str,
        start: float=time.time()
        ):

        self.source_file = source_file
        self.start = start


    def day(self):
        """
        Method that prints the day(s) with the most amount of passings.

        Simply put it takes all the total passings of each day, adds
        that data to a list, and finds the max value and its 
        associated date(s).
        """

        global days_known
        days_known = True
        dict_start = time.time()

        with open(self.source_file, 'r') as data_file:
            print(f'\rLoading simulation data...',end=' ')
            data = json.load(data_file)
            data = data["data"]
            days = []
            days_data = []

            for year in range(len(data)):
                day_count = 1

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

                        day_count += 1
                        print(f'\rComparing days: {day_count}/365  '
                        + f' in year: {2022+year}', end=' ')

            while True:
                max_day_index = days.index(max(days))
                max_day_int = days[max_day_index]
                max_day_data = days_data[max_day_index]

                max_days.append(max_day_data)

                del days[max_day_index]
                del days_data[max_day_index]

                if days[days.index(max(days))] < max_day_int:
                    break

            print(
                f'\rData analyzed.        Elapsed time:   '
                + f'{round(time.time() - dict_start)}s  '
                + f'                                 '
            )
            print(
                f'\nThe maximum amount of passings in a day was:'
                + f' {max_day_int}\n'
                + f'The day(s) with this amount of passings was:'
            )
            for i in range(len(max_days)):
                print(
                    f'   {max_days[i]["month"]} {max_days[i]["day"]}. '
                    + f'{max_days[i]["year"]}'
                )
        
    
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
                    f'\nThe {max_days[i]["day"]}. {max_days[i]["month"]}'
                    + f'  {max_days[i]["year"]} the hour(s)'
                    + f' with the most passings was:\n'
                )
                
                for k in range(len(max_hours)):
                    print(f'\t{max_hours[k]}:00-{max_hours[k]+1}:00')
                
                print(f"\nThe number was : {max_hour_int}")


see_help_main()
if __name__ == "__main__":
    CURRENT_DIR = __file__[:len(__file__) - len("main.py")]
    display = Display(
        source_file = CURRENT_DIR + "/simulator/data.txt"
    )

    register = Register(
        target_file = CURRENT_DIR + "/register/register.txt",           
        models_file = CURRENT_DIR + "/register/resources/models.csv",
        names_file = CURRENT_DIR + "/register/resources/names.csv",

        amt = 100000    # ? Amount of cars to fill the register with 
                        # ! MAXIMUM 100'000
    )

    simulator = Simulator(

        min = 10,       # ? Minimum cars per hour
        max = 100,      # ? Maximum cars per hour
        years = 1,      # ? Years to run the simulation

        target_file = CURRENT_DIR + "/simulator/data.txt",
        source_file = CURRENT_DIR + "/register/register.txt"
    )

    lines = [
        ["\n\nREAD!!!", .5], 
        ["The register is already filled, and a tracked simulation", .1],
        ["has already been run, but you can OPTIONALLY run both", .1],
        ["these scripts to test that they work.\n", .1],
        ["By default there is 100'000 different cars/persons in", .1],
        ["the register and the simulation simulates 1 year (8760 hours)", .1],
        ["of between 10 and 100 cars passing by each hour.", .1]
    ]

    for line in range(len(lines)):
        print(lines[line][0])
        time.sleep(lines[line][1])

    time.sleep(0.5)
    valid = False

    while valid == False:
        time.sleep(0.5)
        gen_register = str(input(
            f"\nFill the register with 100'000 random cars? [y/n] : "
        ))

        if gen_register == "y" or gen_register == "Y":
            register.create_register_obj()
            register.dump_json()
            valid = True

        elif gen_register == "n" or gen_register == "N":
            valid = True

        else:
            print("\nInvalid input")
    
    valid = False

    while valid == False:
        time.sleep(0.5)
        simulate = str(input(
            f"\nSimulate cars passing registration point for "
            + f"({simulator.years}) year(s)? [y/n] : "
        ))

        if simulate == "y" or simulate == "Y":
            simulator.simulate()
            simulator.dump_json()
            valid = True

        elif simulate == "n" or simulate == "N":
            valid = True

        else:
            print("\nInvalid input")

    display.day()
    #display.hour()

    print("\n\nProgram done.")