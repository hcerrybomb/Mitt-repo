from pylab import *                                  #importere de nødvendige biblotekene

a = -6                                                #definerer første intervall   

b = 0                                                #definerer andre intervall      

e = 0.0001                                           #definerer hvor nærme null resultatet kan være for å bli ansett som et nullpunkt
                                          
def f(x):                                            #lager en funksjon for f(x)
        
    #return x**2 - 6*x + 8                           #gjør at når du kaller på f(x) i programmet får du denne funksjonen
    return x**3+6*x**2+11*x+6
m = (a + b)/2.                                       #definere m som midtpunktet i intervallet [a, b]
                                            
while abs(f(m)) >= e:                                #lager en loop som kjører så lenge resultat av abs(f(m)) ikke er nærme nok null

    if f(a)*f(m) < 0:                                #sjekker om nullpunktet ligger i intervallet [a, m]

        b = m                                        #om det gjør det endrer det intervallet til [a, b] ved å flytte b til verdien av m   
               
    else:                                            #om nullpunktet ikke er i intervallet [a, m] 
                                                      
        a = m                                        #endrer det intervallet [a, b] ved å flytte a til verdien av m 
                            
    m = (a + b)/2                                    #definerer igjen m som midtpunkt mellom [a, b] siden intervallet ble endret 
             
print("Nullpunktet er tilnærmet lik ", round(m, 2))  #printer m når f(m) er nærme nok null til å bli et midtpunkt