blå = '\x1b[0;36;49m'
ingen = '\x1b[0m'
rød = '\x1b[0;29;41m'
anmeldelser = []
LeggTil = input("vil du legge til en vurdering?(ja/nei): ")
while LeggTil == "ja":
   vurdering = int(input("vurder filmen fra 1-10: "))
   if vurdering in range(1,11):
       anmeldelser.append(vurdering)
       print(" ")
       print("============================================")
       print("din vurdering er lagt til")
       print("============================================")
       LeggTil = input("vil du legge til en ny vurdering?(ja/nei): ")
   else:   
       while not vurdering in range(1,11):
           print(" ",rød)
           print(" ERROR:",ingen,"det tallet er ikke mellom 1 og 10")
           vurdering = int(input("vurder filmen fra 1-10: "))
       else:
           anmeldelser.append(vurdering)
           print(" ")
           print("============================================")
           print("din vurdering er lagt til")
           print("============================================")
           LeggTil = input("vil du legge til en ny vurdering?(ja/nei): ")
else:
    Sum = sum(anmeldelser)
    Antall = len(anmeldelser)
    gjennomsnitt = Sum / Antall
    gjennomsnitt = round(gjennomsnitt, 2)
    print(" ")
    print("============================================")
    print("antall vurderinger:",blå,Antall,ingen)
    print("gjennomsnittlig vurdering er:",blå,gjennomsnitt,ingen,"/ 10")
    print("============================================")