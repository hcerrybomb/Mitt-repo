#%%
from pylab import * 

nordsør = loadtxt("nordsoor.csv",
                  delimiter=";",
                  skiprows=1, 
                  usecols = range(0,3))

år = nordsør[:,0]
nord = nordsør[:,1]
sør = nordsør[:,2]


plot(år, nord)
plot(år, sør)

print(år, nord, sør)


plot(år[12:-1], nord[12:-1])
plot(år[12:-1], sør[12:-1])
ylim(0,2000000)

# %%
from pylab import *
import numpy as np

nordsørtorsk = loadtxt("nordsoortorsk.csv",
                encoding="utf-16",
                  delimiter=";",
                  skiprows=2, 
                  usecols = range(0,3))

år = nordsørtorsk[:,0]
nordtorsk = nordsørtorsk[:,1]
sørtorsk = nordsørtorsk[:,2]

fig1, (ax1, ax2) = subplots(1,2)
fig1.tight_layout(h_pad=2)


ax1.plot(år, nordtorsk, c="red")
ax2.plot(år, sørtorsk, c="blue")
print(len(år))

x = np.array(år[10:len(år)])
y = np.array(sørtorsk[10:len(sørtorsk)])

ax2.plot(x,y,'o')


m, b = np.polyfit(x,y,1)

print(x)
print(m*x+b)
ax2.plot(x, m*x + b, linewidth=3)


fig2, (ax1, ax2) = subplots(1,2)
fig2.tight_layout(h_pad=2)



nordtemp = loadtxt("temp-nord.csv", delimiter=";", skiprows=1, usecols=range(0,11))

år = nordtemp[:,0]
avrg = nordtemp[:,10]

for i in range(1,10):
    #print(f"INDEX NUMBER {i}: {nordtemp[:,i]}")
    ax1.plot(nordtemp[:,0], nordtemp[:,i])

ax1.plot(år, avrg, linewidth=3, color="black")


sørtemp = loadtxt("temp-soor.csv", delimiter=";", skiprows=1, usecols=range(0,5))

år = sørtemp[:,0]
avrg = sørtemp[:,4]

for i in range(1,4):
    #print(f"INDEX NUMBER {i}: {nordtemp[:,i]}")
    ax2.plot(sørtemp[:,0], sørtemp[:,i])

ax2.plot(år, avrg, linewidth=3, color="black")

# %%

# %%
