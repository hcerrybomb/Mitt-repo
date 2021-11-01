from sympy import symbols, solve
from sympy import *
x = symbols('x')
expr = N(x ** 2 - 3) 
var1 = solve(expr)
svar1 = var1[0]
svar2 = var1[-1]
float(svar1)
float(svar2)
svar1 = round(svar1, 3)
svar2 = round(svar2, 3)
blå = '\x1b[0;36;49m'
ingen = '\x1b[0m'
print(" ")
print(" for",blå,"x",ingen,"^ 2 - 3 = 0")
print(" ")
print(blå,"x",ingen,"=",blå,svar1,ingen,"/",blå,svar2,ingen)