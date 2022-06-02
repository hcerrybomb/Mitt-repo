#%%
from pylab import * 
import numpy as np

nordsør = loadtxt("nordsoor.csv", delimiter=";", skiprows=1, usecols = range(0,3))

år = nordsør[:,0]
nord = nordsør[:,1]
sør = nordsør[:,2]


plot(år, nord)
plot(år, sør)

title("Total fisk i tonn - \nnord (blå) og sør (sør) for polarsirkelen")
grid()
xlabel("År")
ylabel("Fisk")


##################################################


nordsørtorsk = loadtxt("nordsoortorsk.csv", encoding="utf-16", delimiter=";", skiprows=2, usecols = range(0,3))

år = nordsørtorsk[:,0]
nordtorsk = nordsørtorsk[:,1]
sørtorsk = nordsørtorsk[:,2]

################################################

fig1, (ax1, ax2) = subplots(1,2, constrained_layout=True)
fig1.suptitle('Antall torske fisk i tonn')


ax1.plot(år, nordtorsk, c="blue")

x = np.array(år[13:len(år)])
y = np.array(nordtorsk[13:len(nordtorsk)])

ax1.plot(x,y,'o')

m, b = np.polyfit(x,y,1)
ax1.plot(x, m*x + b, linewidth=3, c="orange")
ax1.set_title("Nord for polarsirkelen")
ax1.set_xlabel("År")
ax1.set_ylabel("Torske fisk i tonn")


ax2.plot(år, sørtorsk, c="blue")

x = np.array(år[10:len(år)])
y = np.array(sørtorsk[10:len(sørtorsk)])

ax2.plot(x,y,'o')

m, b = np.polyfit(x,y,1)
ax2.plot(x, m*x + b, linewidth=3, c="orange")
ax2.set_title("Sør for polarsirkelen")
ax2.set_xlabel("År")



##############################################



fig2, (ax1, ax2) = subplots(1,2, constrained_layout=True, sharey=True)
fig2.suptitle('Temperatur sør/nord for polarsirkelen - \n i utvalgte fylker')



nordtemp = loadtxt("temp-nord.csv", delimiter=";", skiprows=1, usecols=range(0,11))

år = nordtemp[:,0]
avrg = nordtemp[:,10]

for i in range(1,10):
    ax1.plot(nordtemp[:,0], nordtemp[:,i])

ax1.plot(år, avrg, linewidth=3, color="black")
ax1.set_title("Nord for polarsirkelen")
ax1.set_xlabel("År")
ax1.set_ylabel("Temperatur (C)")
ax1.set_ylim(-2,2)

sørtemp = loadtxt("temp-soor.csv", delimiter=";", skiprows=1, usecols=range(0,5))

år = sørtemp[:,0]
avrg = sørtemp[:,4]

for i in range(1,4):
    ax2.plot(sørtemp[:,0], sørtemp[:,i])

ax2.plot(år, avrg, linewidth=3, color="black")
ax2.set_title("Sør for polarsirkelen")
ax2.set_xlabel("År")


