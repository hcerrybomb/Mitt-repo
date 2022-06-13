#%%
#test
from pylab import *

inflasjon = loadtxt("inflasjon.csv", delimiter=";",skiprows = 1, usecols = (1,2))
år = inflasjon[:,0]
infl_prosenter = inflasjon[:,1]

grunnverdi = 1 
valuta_økning = []
for i in range(len(år)):
    print(f"verdi før økning: {round(grunnverdi,2)}")

    grunnverdi += grunnverdi * infl_prosenter[i] / 100
    print(f"prosent økning: {infl_prosenter[i]}%")
    print(f"verdi etter økning: {round(grunnverdi,2)}")
    
    valuta_økning.append(grunnverdi)
    print(" ")

plot(år, valuta_økning)
grid()
xlabel("år")
ylabel("valuta økning")

# %%
