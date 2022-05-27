#%% 
from pylab import *
import statsmodels.api as sm

yrke = loadtxt("fisker-yrke.csv", delimiter=";",skiprows = 1, usecols = range(0,4))



år = yrke[:,0]
hovedyrke = yrke[:,1]
sideyrke = yrke[:,2]
totalyrke = yrke[:,3]

figure, (ax1, ax2) = subplots(1,2, sharey=True)

ax1.plot(år, hovedyrke, color="red")
ax1.plot(år, sideyrke, color="blue", linestyle="dashed")
ax1.set_ylabel("yrkesfiskere")
ax1.set_xlabel("år")
ax1.axvline(x=1969,ymin=0.06, ymax=0.5, color="k",linewidth=2)
ax1.set_title("hoved (rød) og sideyrke (blå)")



ax2.plot(år, totalyrke, color="red")
ax2.axvline(x=1969,ymin=0.2, ymax=0.6, color="k",linewidth=2)
ax2.set_title("total")
ax2.set_xlabel("år")


 # %%
