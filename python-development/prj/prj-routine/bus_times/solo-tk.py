import datetime
import time
import tkinter as tk
import tkinter.ttk as ttk



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



current_time, hrs_till, mins_till, secs_till = get_time()



window1 = tk.Tk()





button1 = tk.Button(
    text = "Click",
    width = 24,
    height = 12,
    #fg = "HEXHEX"

)


label1 = ttk.Label(
    text="hihhih hello",
    #fg ="#HEXHEX",
    #width = 10
    #height = 10
    #width and height are measured in text units. One horizontal text unit is determined by the width of the character 0

)
entry1 = tk.Entry(
    fg="yellow",
#   bg="blue"
    width=50
)


text1 = tk.Text()


label1.pack()
button1.pack()
entry1.pack()
text1.pack()

inputvar1 = entry1.get()
entry1.delete(0,tk.END)
entry1.insert(0,"hihhihiehih")


window1.mainloop()

if False:
    window1.destroy()