from pylab import *



a = float(input("Skriv inn koeffisienten foran x^2-leddet: "))
b = float(input("Skriv inn koeffisienten foran x-leddet: "))
c = float(input("Skriv inn konstantleddet: "))
x = linspace(-10, 10, 1001)
y = a*x**2 + b*x + c
plot(x, y, "m")


d = b**2-4*a*c

if d > 0:
    Svar1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    Svar2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print(" ")
    print("Nullpunkt 1 =", Svar1)
    print("Nullpunkt 2 =", Svar2)


elif d == 0:
    Svar1 = -b/(2*a)
    print(" ")
    print("Nullpunkt =", Svar1)
    
else:
    print(" ")
    print("Ingen løsning")


axhline(y=0, color="k") 
axvline(x=0, color="k") 



show()  