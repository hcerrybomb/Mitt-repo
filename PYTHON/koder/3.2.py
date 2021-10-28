blå = '\x1b[0;36;49m'
rød = '\x1b[0;29;41m'
ingen = '\x1b[0m'
error = '\x1b[5m'
totalpris = 0
NyBruker = "ja"
antallbillett = 0
while NyBruker == "ja":        
   var1 = int(input("Hvor gammel er du(bare tall)?: "))
   prisunder6 = 0
   prisunder17 = 19
   prisover18 = 37
   prisover67 = 19
   pris = int
   totalpris = totalpris
   if int(var1) in range (0,6):
       pris = prisunder6
   elif int(var1) in range (6,17):
       pris = prisunder17
   else:
       if int(var1) in range (18,67):
           pris = prisover18
       elif int(var1) in range (67,150):
           pris = prisover67
       else:           
           pris = -2
   if pris > 0:     
       soner = int(input("hvor mange soner(1-4)?: "))
       if 0 < soner < 5:
         if pris == 19:
            pris = pris + 12*soner - 12
         elif pris == 37:
            pris = pris + 24*soner - 24 
         totalpris = totalpris + pris
         antallbillett += 1
         print(" ")
         print("===================================================")
         print("billetter registrert:",blå,antallbillett,ingen,"billetter")
         print("din pris er:",blå,pris,ingen,"kr")
         print("totalprisen for alle passasjerene hittil er:",blå,totalpris,ingen,"kr")
         print("===================================================")    
         NyBruker = input("vil du legge til en billett?(ja/nei): ")    
       else:
          while not 0 < soner < 5:
              print(" ")
              print("===================================================",rød)
              print("ERROR:",ingen,"det er ikke et gyldig antall soner")
              print("===================================================")
              soner = int(input("hvor mange soner(1-4)?: "))
          else:
              if pris == 19:
                  pris = pris + 12*soner - 12
              elif pris == 37:
                  pris = pris + 24*soner - 24
              totalpris = totalpris + pris
              antallbillett += 1
              print(" ")
              print("===================================================")
              print("billetter registrert:",blå,antallbillett,ingen,"billetter")
              print("din pris er:",blå,pris,ingen,"kr")
              print("totalprisen for alle passasjerene hittil er:",blå,totalpris,ingen,"kr")
              print("===================================================")
              NyBruker = input("vil du legge til en billett?(ja/nei): ")
   else:
       if pris == 0:  
          antallbillett += 1
          print(" ")
          print("===================================================")
          print("billetter registrert:",blå,antallbillett,ingen,"billetter")
          print("din pris er:",blå,pris,ingen,"kr")
          print("totalprisen for alle passasjerene hittil er:",blå,totalpris,ingen,"kr")
          print("===================================================")
          NyBruker = input("vil du legge til en billett?(ja/nei): ") 
       elif pris == -2:                     
          print(" ")
          print("===================================================",rød)
          print("ERROR:",ingen,"det er ikke en gyldig alder")
          print("===================================================")  
else:
    if NyBruker == "nei":
        print(" ")
        print("===================================================")
        print("billetter registrert:",blå,antallbillett,ingen,"billetter")
        print("totalprisen for alle passasjerene er:",blå,totalpris,ingen,"kr")
        print("===================================================")
    else:
        print(" ")
        print("===================================================",rød)
        print("ERROR:",ingen,"det er ikke ett gyldig svar")
        print("===================================================")
        print(" ")
        print("===================================================")
        print("billetter registrert:",blå,antallbillett,ingen,"billetter")
        print("totalprisen for alle passasjerene er:",blå,totalpris,ingen,"kr")
        print("===================================================")
        