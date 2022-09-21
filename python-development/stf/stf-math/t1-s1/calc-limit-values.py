#%%
from pylab import *
import time
def f(x):
    return 3*(x**2-4)/(x-2)

print(f(199))

x=1
while x<2:
    print(x,f(x))
    x=x+0.01
    time.sleep(0.01)
    plot(x,f(x),"o")


# %%
