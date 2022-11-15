import math as m



class Planet:
    """
    HELP
    """
    def __init__(
        self, 
        navn:str, 
        solavstand:float, 
        radius:float, 
        antallRinger:int = 0
        ):

        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        self.antallRinger = antallRinger
    
    def visInfo(self):
        print(f"Planeten {self.navn} er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")

    
    def volum(self):
        return (4/3) * m.pi * self.radius**3

class Måne(Planet):
    def __init__(self,nyMåneNavn):
        super().__init__()
        self.nyMåneNavn = nyMåneNavn
    def assignMåne(self):
        print(self.navn)




jup = Planet("Jupiter", 778.5, 69911)
print(jup.volum())

jupMåne = Måne("MÅNEN")


