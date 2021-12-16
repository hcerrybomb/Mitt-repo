import time
v = 1.018
innskudd = 10000
K = 250000
år = 0
totalbeløp = 0
print("\n")
while totalbeløp <= K:
 totalbeløp  +=  innskudd
 totalbeløp  *=  v
 år          +=  1
 print(round(totalbeløp,2),"kr\t",år,"år",end="\r")
 time.sleep(0.1)
print("\n\ndet tar",år,"år")