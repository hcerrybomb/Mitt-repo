from pylab import * 
def f(x):
    if 0<x<100:
        return 0 
    elif 100<= x < 500:
        return x*0.15 - 15
    elif x >= 500:
        return 60
    
x = 0.001

antall = 750

nøyaktighet = 1

while x < antall:
    plot(x,f(x),".")
    time.sleep(0.0001)
    x = x + nøyaktighet
print("ferdig")
