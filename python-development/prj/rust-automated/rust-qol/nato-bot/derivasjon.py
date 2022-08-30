#%%
from pylab import *

utfallsrom = list(range(0,50)) 
for x in range(1000):          
    utfall = choice(utfallsrom, size = 5, replace = False)
    if not max(utfall) <= 9:
        print(utfall)



        
# %%
