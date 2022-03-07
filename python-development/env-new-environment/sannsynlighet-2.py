#%%

from pylab import *
utfallsrom = [1,2,3,4,5,6]
f=0
for i in range(1,600):
    k=choice(utfallsrom)
    #print(k)
    if k==6:
        f+=1
print(f"frekvens seksere {f}")

# %%
