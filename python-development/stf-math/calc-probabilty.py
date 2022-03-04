#%%
from pylab import *
antall = 0
for i in range(10000):
    k=randint(1,7)
    if k== 6:
        antall = antall + 1
        plot(i, antall/i, ".")
print(k)
        

# %%
