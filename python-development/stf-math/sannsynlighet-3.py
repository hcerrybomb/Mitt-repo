
#%%
from pylab import *


utfallsrom = [1,2,3,4,5,6]
tolvere = 0
for i in range(36000000):
    
    t1 = choice(utfallsrom)
    t2 = choice(utfallsrom)
    
    s = t1 + t2
    if s == 12:
        tolvere += 1
        
    


# %%
