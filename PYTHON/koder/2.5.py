grønnbak = '\x1b[0;30;42m'
rødbak = '\x1b[0;30;41m'
ingen = '\x1b[0m'
print(" ")
print("sjekk om et tall er et kvadrattall")
SjekkTall = "ja"
while SjekkTall == "ja":
   tall1 = int(input("sett in heltall: "))
   import math
   rot = math.sqrt(tall1)
   rot = float(rot)
   tall1 = float(tall1)
   if tall1%rot == 0:
       print(" ")
       print(grønnbak,"                   ",ingen)
       print("det er et kvadrattall")
       print("kvadratrot:", int(rot))
       print(grønnbak,"                   ",ingen)
   else:
       print(" ")
       print(rødbak,"                         ",ingen)
       print("det er ikke et kvadrattall")
       print(rødbak,"                         ",ingen)
   SjekkTall = input("vil du sjekke ett til tall(ja/nei)?: ")  