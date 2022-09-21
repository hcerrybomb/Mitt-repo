import datetime
import time
import tkinter as tk



today = datetime.date.today()
weekday = datetime.datetime.today().weekday()
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

friday_bus = ["Friday",7,34] if datetime.date.today().isocalendar()[1] % 2 == 0 else ["Friday",9, 19]
 
cases = [
    ["Monday",      7, 34],
    ["Tuesday",     14, 58],
    ["Wednesday",   9, 19],
    ["Thursday",    7, 34],
    friday_bus,
    ["Saturday",    23, 30],
    ["Sunday",      12, 10],
]

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    secs_till = 60 - int(current_time[6:8])

    hrs_till = cases[weekday][1] - int(current_time[0:2])

    if hrs_till < 0:
        hrs_till = 0
        mins_till = 0
        secs_till = 0
    else: 

        if cases[weekday][2] > int(current_time[3:5]): 
            mins_till = cases[weekday][2] - int(current_time[3:5]) - 1
        else:
            if hrs_till != 0: 
                hrs_till -= 1
                mins_till = 60 - int(current_time[3:5]) + cases[weekday][2] - 1
            else:
                mins_till = 0
                secs_till = 0
    return current_time, hrs_till, mins_till, secs_till


def make_text():
    current_time, hrs_till, mins_till, secs_till = get_time()

    made_text = f"It is {cases[weekday][0]}, {today}, {current_time} \nbus leaves in {hrs_till}hrs {mins_till}mins {secs_till}secs"
    l.config(text=made_text, fg="red")
    root.after(1000, make_text)


root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())

l = tk.Label(text='', font=("Helvetica", 60))
l.pack(expand=True)

def testing():
    print("hihhihelo")

def run():
    make_text()
    root.mainloop()

if __name__ == "__main__":
    run()











