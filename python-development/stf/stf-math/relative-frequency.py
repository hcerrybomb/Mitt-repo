#%%
from pylab import *

N = 10000
terningkast = []

for i in range(N):
    terningkast.append(randint(1,7))

terningkast = array(terningkast)
n = sum(terningkast == 6)
rel_frekv = n/N
print("antall kast:", N)
print("antall seksere: ", n)
print("relativ frekvense: ", rel_frekv)
# %%
