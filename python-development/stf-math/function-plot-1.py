# TEST 1

from pylab import *
x = linspace(-5, 7, 1000)
def funksjonsverdi(x):
    y = x**3 - 4*x**2 - 9*x + 28
    return y 

y = funksjonsverdi(x)


plot(x, y, "b")


