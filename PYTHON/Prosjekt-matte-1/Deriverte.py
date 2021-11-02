from pylab import *
import numpy
x = linspace(-4, 6, 1000)  #   <--- bør endres basert på funksjonen

delta_x = 0000.1
          
def funksjonsverdi(x):              
#    y = x**3 - 4*x**2 - 9*x + 28       #ORGINALT EKSEMPEL
#    y = 2*x**3 - 3*x**2 - 7*x + 20     #EGET TREDJEGRADSEKSEMPEL EKSEMPEL
#    y = 2*x**2 + 3*x - 2               #ANDREGRADS EKSEMPEL
#    y = e**(2*x+1) - 1                 #EKSPONENTIELL EKSEMPEL
    y = np.log(x)*(x**2 - 3*x)             #SAMMENSATT FUNKSJON EKSEMPEL
    return y           

def derivert(x):
    dy = (funksjonsverdi(x + delta_x) - funksjonsverdi(x)) / delta_x
    return dy

def dobbelderivert(x):
    x = x[0:1000-1]
    ddy = (derivert(x + delta_x) - derivert(x)) / delta_x
    return ddy

y = funksjonsverdi(x) 
dy = derivert(x)
ddy = dobbelderivert(x)
axhline(y=0, color="k") 
axvline(x=0, color="k") 
xlabel("X")
ylabel("Y")
grid()
xlim(-4, 6)#   <--- bør endres basert på funksjonen
ylim(-5, 10)#   <--- bør endres basert på funksjonen
plot(x, y, "b", label = "f(x)")    
plot(x, dy, "r", label = "f'(x)")
plot(x[0:1000-1], ddy, "g", label = "f''(x)")
legend()
show()                        
import sys
print("1")
print(sys.version)
print("2")