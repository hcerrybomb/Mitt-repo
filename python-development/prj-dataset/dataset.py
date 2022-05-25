#%%
from pylab import *

median = [40300, 41200, 42180, 43400, 45000]
nedre = [33300, 34100, 34980, 35840, 37180]
øvre = [50100, 50900, 52250, 53910, 55870]
år = [2015, 2016, 2017, 2018, 2019]

plot(år, median, "r")
plot(år, nedre, "b--")
plot(år, øvre, "b--")

xlabel("År")
ylabel("Månedslønn (kr)")
ylim(30000, 60000)

#? programmet plotter statistikken for median, øvre og nedre verdier for mpnedslønnen i årene 2015-2019



økn_median = 100 * ((median[4] - median[0]) / median[0])
økn_nedre = 100 * ((nedre[4] - nedre[0]) / nedre[0])
økn_øvre = 100 * ((øvre[4] - øvre[0]) / øvre[0])

print("Økning av medianlønna:", round(økn_median, 1), "%")
print("Økning for nedre kvartil:", round(økn_nedre, 1), "%")
print("Økning for øvre kvartil:", round(økn_øvre, 1), "%")

#? Programmet sier nå også økningen i prosent for alle verdiene av funksjonene som datasetter viser i intevallene



# %%
from pylab import *

andel_jenter = [7, 23, 21, 45, 27, 37, 41, 53, 47, 49, 69, 68, 55, 68, 69, 64, 78, 73]
år = list(range(2003, 2021))

plot(år, andel_jenter)
xlabel("År")
ylabel("Andel handlet i %")
xlim(2003, 2020)
ylim(0, 100)


#? progammet plotter statistikken for andel jenter per år i et intervall mellom 2004 og 2020



k = 2                             
b = len(andel_jenter) - k
glatt = [ ] 

for i in range(k, b): # beregner de glattede verdiene
  glatt.append(mean(andel_jenter[(i - k):(i + k)]))

plot(år[k:len(andel_jenter) - k], glatt)


#? om man endrer verdien til K så endrer man intervallet for begge sidene av plotten for de glattede verdiene
#? mean() beregner gjennomsnittet i en array, len() er lengen i en array


# %%


#? .csv filen er et datasett med en tabell av verdier koblet til et år

from pylab import *

hopen = loadtxt("hopen.csv", delimiter=";",skiprows = 1, usecols = (2,3))
aar =  hopen[:,0]
temp= hopen[:,1]

plot(aar, temp)
xlabel("År")
ylabel("Temperatur")

#? progammet plotter dataen fra .csv filen for temperaturen i et gitt år i intervallet 1950 og 2020

print(hopen)
# %%
from pylab import *
import statsmodels.api as sm
lowess = sm.nonparametric.lowess

hopen = loadtxt("hopen.csv", delimiter=";",skiprows = 1, usecols = (2,3))
år =  hopen[:,0]
temp= hopen[:,1]

plot(år, temp)
xlabel("År")
ylabel("Temperatur")

glatt = lowess(temp, år, frac = 0.2, return_sorted=False)
plot(år, glatt)


#? programmet viser at den generelle temperaturen på Svalbard (Hopen) har økt substansiellt i de siste årene

# %%
from pylab import *
import statsmodels.api as sm

hopen = loadtxt("hopen.csv", delimiter=";",skiprows = 1, usecols = (2,3))
år =  hopen[:,0]
temp= hopen[:,1]

plot(år, temp)
xlabel("År")
ylabel("Temperatur")

k = 5
glatt =[]

for i in range(k,len(temp)-k):
    glatt.append(mean(temp[(i-k):(i+k)]))
    
plot(år[k:len(temp)-k], glatt, "k")

#? den svarte linja er statistikken for den gjennomsnittlige verdien for temperatur i et intervall av 10 år får hvert år.

#? altså den første verdien har intervallet [1946, 1956] og programmet plotter den gjennomsnittlige verdien av de 10 årene på midten av intervallet, altså 1951. 
#? slik gjør den for hvert år framover, altså plotter den den gjennomsnittlige temperaturen for [1947, 1957] i året 1952, osv osv. 



#%%
from pylab import *
import statsmodels.api as sm
alna = loadtxt("alna.csv", 
               delimiter=";",
               skiprows = 1, 
               usecols = (3,4))

temp= alna[:,0]
vind = alna[:,1]
måned = range(1,92)




figure, axis = subplots(2,2)


axis[0, 0].plot(måned, temp, "r")
axis[0, 0].set_title("EXAMPLE TEST")
xlabel("Måneder 2007-2015")
ylabel("Temperatur / Vind")

#axis[0, 0].plot(måned, vind, "g")
#axis[0, 0].xlabel("Måneder 2007-2015")
#axis[0, 0].ylabel("Temperatur / Vind")

k = 2
glatt =[]

for i in range(k,len(vind)-k):
    glatt.append(mean(vind[(i-k):(i+k)]))


axis[0, 1].plot(måned[k:len(vind)-k], glatt, "b")
#axis[0, 1].xlabel("Måneder 2007-2015")
#axis[0, 1].ylabel("Temperatur / Vind")

axis[1, 0].plot(måned[k:len(vind)-k], glatt, "b")
#axis[1, 0].xlabel("Måneder 2007-2015")
#axis[1, 0].ylabel("Temperatur / Vind")

axis[1, 1].plot(måned[k:len(vind)-k], glatt, "b")
#axis[1, 1].xlabel("Måneder 2007-2015")
#axis[1, 1].ylabel("Temperatur / Vind")

#print(vind)
#plot(måned,vind, "g")


# %%
