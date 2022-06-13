#%%
from pylab import *

import statsmodels.api as sm

ramme, (rad1, rad2, rad3) = subplots(3)


inflasjon = loadtxt("inflasjon.csv", delimiter=";",skiprows = 1, usecols = (1,2))

infl_år = inflasjon[:,0]

infl_prosenter = inflasjon[:,1]


grunnverdi = 1

valuta_økning = []

for i in range(len(infl_år)):
   print(f"verdi før økning: {round(grunnverdi,2)}")

   grunnverdi += grunnverdi * infl_prosenter[i] / 100
   print(f"prosent økning: {infl_prosenter[i]}%")
   print(f"verdi etter økning: {round(grunnverdi,2)}")
  
   valuta_økning.append(grunnverdi)
   print(" ")


rad1.plot(infl_år, valuta_økning)
rad.set_ylim()

rad1.grid()

rad1.set_xlabel("År")

rad1.set_ylabel("valuta økning")


nedre = loadtxt("nedre.csv", delimiter=";",skiprows = 1, usecols = (1,2))

nedre_år =  nedre[:,0]

nedre_tall = nedre[:,1]


rad2.plot(nedre_år, nedre_tall)

rad2.grid()

rad2.set_xlabel("År")

rad2.set_ylabel("Verdi i euro")


dyrest = loadtxt("dyrest.csv", delimiter=";",skiprows = 1, usecols = (1,2))

dyreste_år =  dyrest[:,0]

dyrest_tall = dyrest[:,1]


rad3.plot(dyreste_år, dyrest_tall)

rad3.grid()

rad3.set_xlabel("År")

rad3.set_ylabel("Verdi i euro")




ramme.tight_layout()