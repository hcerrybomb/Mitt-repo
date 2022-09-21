import sys
import time
def progress(count, total, status=''):
    red='\033[01;31m'
    gre='\033[02;32m'
    yel='\033[00;33m'
    blu='\033[01;34m'
    
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    
    percentage = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    
    
    if percentage <= 50:
        col = red
    elif percentage > 50 and percentage <= 80:
        col = yel
    elif percentage > 80 and percentage <= 99:
        col = gre
    else:
        col = blu
    
    sys.stdout.write('\r{0}{1} {2} {3}   {4}'.format(col, round(percentage), bar, total, status))
    sys.stdout.flush()

for i in range(101):
    time.sleep(1)
    progress(i, 100, status="song name")