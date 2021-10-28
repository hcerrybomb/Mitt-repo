
#lest = 22+6
LestNu = int(input("Antall kapitler lest totalt: "))
Total =LestNu
del1 = 63
del2 = 30
del3 = 18
if Total <= 63:
    print("du har",  del1-Total, "kapitler igjen av del 1")
if del1 + del2 > Total > 63:
    print("du har", del1+del2-Total, "kapitler igjen av del 2")
if del1+del2+del3 > Total > del1+del2:
    print("du har igjen", del1+del2+del3 - Total, "kapitler igjen av del 3")
print("du har lest ", Total, "kapitler av ", del1+del2+del3)        