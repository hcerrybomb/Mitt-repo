faktorer = []
num = int(input("skriv in tall: "))

if num % 2 == 0:
    print("taller er delelig på 2")
if num % 3 == 0:
    print("taller er delelig på 3")
if num % 5 == 0:
    print("tallet er delelig på 5")
import numpy
def print_faktor(x):
    print("faktorene til", num, "er: ")
    for i in range (1, x):
        if x % i == 0:
            print(i)
            print("*")
            faktorer.append(i)
print_faktor(num)
tall = numpy.prod(faktorer)
print("=")
print(tall)



