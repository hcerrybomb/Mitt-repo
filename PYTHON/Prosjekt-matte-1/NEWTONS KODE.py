from pylab import *
import time 

x = linspace(-3, 4, 100000) # Verdier for x  <--- bør endres baser på hvilken funksjon du velger

delta_x = 0.000001 # Setter nøyaktigheten til delta_x, <--- tweaket her

def f(x): # Funksjon som regner ut y-verdiene
#    y = x**3 - 4*x**2 - 9*x - 28       # Funksjonen        
#    y = x**3 - 4*x**2 - 9*x + 28       #ORGINALT EKSEMPEL
#    y = 2*x**3 - 3*x**2 - 7*x + 20     #EGET TREDJEGRADSEKSEMPEL EKSEMPEL
#    y = 2*x**2 + 3*x - 2               #ANDREGRADS EKSEMPEL
#    y = (-4*x+79)/x                  #RASJONAL FUNKSJON
#    y = e**(2*x+1) - 1                 #EKSPONENTIELL EKSEMPEL
    y = log(x)*(x**2 - 3*x)             #SAMMENSATT FUNKSJON EKSEMPEL    
    return y # Returnerer funksjonsverdiene

def derivert(x): # Funksjon som regner ut den deriverte
    # Bruker definisjonen til den deriverte
    dy = (f(x + delta_x) - f(x)) / delta_x
    return dy # Returnerer funksjonsverdiene

def ny_x_verdi(x1): # Tar inn x-verdien x1
    # Regner ut med Newtons formel
    x2 = x1 - (f(x1) / derivert(x1))
    return x2 # Returnerer ny verdi for x1

y = f(x) # Kaller på funksjonen funksjonsverdi
dy = derivert(x)
plot(x, y, "b") # Plotter funksjonen blå
plot(x, dy, "r")
xlabel("x") # Pynter på grafen her
ylabel("y")
grid()
ylim(-7, 7)     #  <--- bør endres basert på hvilken funksjon du velger
axhline(y=0, color="k")
axvline(x=0, color="k")
show()
x1 = float(input("Skriv inn x-verdi nær nullpunktet: "))
x2 = ny_x_verdi(x1) # Kaller på funksjonen
while abs(x2-x1) > delta_x: #sjekker om forskjellen mellom x2 og x1 er lav nok til å møte den ønskede nøyaktigheten
    x1 = x2 # "resetter" løkken ved å sette det nye forslaget tilbake i formelen
    x2 = ny_x_verdi(x1) #regner ut formelen med det nye forslaget 
    print("Et bedre forslag er gitt ved x = ", (x2))
    time.sleep(0.1)
    
print("nullpunktet er ved x = ", round(x2, 3))
