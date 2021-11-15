class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BLINK = '\33[5m'
print(style.CYAN + "\nwhat time is wipe for you?"+style.RESET+"\n\ngive your answer in an 00:00 format\n\nexamples:\n\n    17:00\n    15:30\n    04:45\n\n")
UserInput = str(input("give your answer here:   "))

print(len(UserInput))

def errorcheck():
    if len(UserInput)>5:
        print("\n too few charcters")
    if UserInput.count(":")<1:
        print("you forgot the colon")
    if len(UserInput)<5:
        print("too few characters")
