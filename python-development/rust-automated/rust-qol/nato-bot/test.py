#%%
from pylab import *
a = -10
b = 10
dx = 0.2


def f(x):
    return 2*(x**2-1)**2

for x in range(a, b):
    plot(x,f(x),".r")
    dy=f(x+dx)-f(x-dx)
    plot(x, dy/dx, ".b")
# %%
