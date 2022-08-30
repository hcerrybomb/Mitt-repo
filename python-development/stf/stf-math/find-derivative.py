#  ---  Der of function ---
from sympy import symbols, solve
from sympy import *

x = symbols('x')

y = log(x)*(x**2 - 3*x)
DER = diff(y)
print(DER)



