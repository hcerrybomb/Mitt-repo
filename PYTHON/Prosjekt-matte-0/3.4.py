# og forklaring bak hver linje i koden under 

primtall = [] #lager en liste kalt "primtall"

for muligePrimtall in range(2, 100): #kjører loopen med verdiene for "muligePrimtall" mellom 2 og 100

    erPrimtall = True #omgjør variablen "erPrimtall" til true

    for num in range(2, muligePrimtall): #kjører loopen med verdiene for "num" mellom 2 og variablen "muligePrimtall"

        if muligePrimtall % num == 0: #kjører loopen om variablen resten av "muligePrimtall" delt på "num" er 0

            erPrimtall = False #gjør variablen "erPrimtall" om til false

            break #slutter loopen

 

    if erPrimtall: #kjører loopen om variablen "erPrimtall" er true

        primtall.append(muligePrimtall) #legger til "muligePrimtall" i listen "primtall"

print(primtall) #printer listen "primtall"