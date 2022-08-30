blå = '\x1b[0;36;49m'
rød = '\x1b[0;29;41m'
ingen = '\x1b[0m'
programnavn = input("hva heter du?: ")
print(" ")
print("===============")
print("hei", programnavn)
print("===============")
kjør = 0
månedslønn = 0
totaltimer = 0
float(månedslønn)
lønn = int
RegUke = "ja"
while kjør != 4:
    if kjør < 4:
       if RegUke == "ja":
          timer = float(input("hvor mange timer jobbet du (bare tall) denne uken?: "))
          print(" ")
          print("=========================================")
          if timer > 0:
              if timer < 166:
                  if timer > 37.5:
                   lønn = 400 * timer
                  else:
                      lønn = (timer * 400) * 0.5
                  lønnmedskatt = lønn - ((lønn/100)*30)
                  print("navn:",blå,programnavn,ingen)
                  print("du jobbet",blå,timer,ingen,"timer denne uken")
                  totaltimer = totaltimer + timer
                  print("du har jobbet totalt:",blå,totaltimer,ingen,"timer")
                  kjør += 1
                  print("uker registrert:",blå,kjør,ingen)
                  print("lønn før skatt:",blå,int(lønn),ingen,"kr")
                  print("lønn etter skatt:",blå,int(lønnmedskatt),ingen,"kr")
                  print("=========================================")
                  månedslønn = månedslønn + lønnmedskatt
                  if kjør == 4:
                      break
                  else:
                      RegUke = input("vil du registrere en ny uke(ja/nei)?: ")
              else:
                  print(rød,"ERROR:",blå,timer,ingen,"er ikke et gyldig antall timer")
                  print("=========================================")
          else:
              print(rød,"ERROR:",blå,timer,ingen,"er ikke et gyldig antall timer")
              print(" ")
              print("=========================================")
       elif RegUke == "nei":
           print(" ")
           print("=========================================")
           print("navn:",blå,programnavn,ingen)
           print("du jobbet totalt:",blå,totaltimer,ingen,"timer")
           print("uker registrert:",blå,kjør,ingen)
           print("lønn før skatt:",blå,int(lønn),ingen,"kr")
           print("lønn etter skatt:",blå,int(lønnmedskatt),ingen,"kr")
           print("ikke nok uker for å kalkulere månedslønn")
           print("=========================================")
           kjør = 5
           break
       else:
           print(" ")
           print("=========================================")
           print(rød,"ERROR:",ingen,RegUke,"er ikke ett gyldig svar")
           print("=========================================")
           RegUke = input("vil du registrere en ny uke(ja/nei)?: ")
if kjør == 4:
   print("du jobbet totalt",blå,totaltimer,ingen,"timer denne måneden")
   print("månedslønn:",blå,int(månedslønn),ingen,"kr")
   print("=========================================")