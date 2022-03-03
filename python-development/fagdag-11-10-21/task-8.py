import random

Heltall = []

antall = 100000

hvilkenpåstand = 3      #velger hvilken påstand du vil sjekke
                        #test programmet så mange ganger du vil
startpunkt = 1

antalltester = 1000

kjøringer = 0

count1 = 0

count2 = 0

x = startpunkt          #for senere funksjonalitet i f.eks def funksjoner

for i in range(antall):
    
    Heltall.append(x)
    
    x = x+1
        
if hvilkenpåstand ==1:
    
   lengderekke = 5

if hvilkenpåstand ==2:
    
   lengderekke = 6

if hvilkenpåstand ==3:
    
   lengderekke = 7
   
Intervall1 = random.randint(1,antall-11)

Intervall2 = Intervall1 + lengderekke     

tall1 = Heltall[Intervall1]

tall2 = Heltall[Intervall2]


if lengderekke == 5:

    while antalltester > kjøringer:

        kjøringer = kjøringer + 1

        total = 0

        for i in range(Intervall1, Intervall2):
            
            total = total + Heltall[i]
        
        if total % 5 == 0:
            
            count1 = count1 + 1
            
            print("sukksessful test nr: ",count1)
            
        else:
            
            count2 = count2 + 1
            
            print("\n\nførste påstanden er ikke sann")
            
        Intervall1 = random.randint(1,antall-11)

        Intervall2 = Intervall1 + lengderekke     
        
        tall1 = Heltall[Intervall1]
        
        tall2 = Heltall[Intervall2]
        
    if count2 == 0:
        
        print(count1," / ",kjøringer,
              "kjøringer var sukksessfulle, påstanden er sant!")
        
    else:
        print(count1," suksessfulle kjøringer\t\t",count2,
              " ikke suksessfulle kjøringer")
        
if lengderekke == 6:
    
    while antalltester > kjøringer:
        
        kjøringer = kjøringer + 1
        
        total = 0
        
        for i in range(Intervall1, Intervall2):
        
            total = total + Heltall[i]

        if total % 6 == 0:
            
            count2 = count2 + 1
        
            print("\n\nandre påstanden er ikke sann")
            
        else:
            
            count1 = count1 + 1
        
            print("suksessful test nr: ",count1)
            
        Intervall1 = random.randint(1,antall-11)

        Intervall2 = Intervall1 + lengderekke     
        
        tall1 = Heltall[Intervall1]
        
        tall2 = Heltall[Intervall2]
        
    if count2 == 0:
        
        print(count1," / ",kjøringer,
              "kjøringer var sukksessfulle, påstanden er sant!")
        
    else:
        print(count1," suksessfulle kjøringer\t\t",count2,
              " ikke suksessfulle kjøringer")
    
    
if lengderekke == 7:
    
    while antalltester > kjøringer:
        
        kjøringer = kjøringer + 1
        
        total = 0
        
        for i in range(Intervall1, Intervall2):
            
            total = total + Heltall[i]
        
        if total % 7 == 0:
            
            count1 = count1 + 1
        
            print("rekken av sju var delelig kjøring nr.",kjøringer)
            
        else:
            
            count2 = count2 + 1
            
            print("rekken av sju var ikke delelig kjøring nr.",kjøringer)
            
        Intervall1 = random.randint(1,antall-11)

        Intervall2 = Intervall1 + lengderekke     
        
        tall1 = Heltall[Intervall1]
        
        tall2 = Heltall[Intervall2]
        
    print("rekken av sju heltall var delelig",count1," / ",
          kjøringer," ganger for",)
    



    
