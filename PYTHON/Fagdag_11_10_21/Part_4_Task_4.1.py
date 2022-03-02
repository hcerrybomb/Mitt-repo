a=0                                                         #definerer første intervall

b=1000                                                      #defnerer andre intervall

riktig="nei"                                                #definerer variablen riktig som "nei"

print("Tenk på et heltall")                                 #printer beskjeden "tenk på et heltall"

while riktig !="ja":                                        #lager en loop som kjører så lenge variablen riktig ikke er "ja"

    m=(a+b)//2                                              #definere variablen m som antallet 2 man finner i a+b

    print("Er tallet du tenker på", m, "?")                 #spør brukeren om tallet de tenker på er variablen m

    riktig=input()                                          #endrer variablen riktig til brukerens input

    if riktig!="ja":                                        #sjekker om variablen riktig ikke er ja

        print("Er tallet du tenker på større enn", m, "?")  #om den ikke er spør den brukeren om tallet deres er større enn variablen m

        svar=input()                                        #definerer en variabel svar til brukerens input

        if svar=="ja":                                      #sjekker om svaret er ja

            a=m                                             #om det er det endrer den variablen a til verdien av m

        else:                                               #om den ikke 

            b=m                                             #endrer den variablen b til verdien av m 