class Bruker:
    """ Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
    
    """
    def __init__(self, epost, fornavn, etternavn):
        self.epost = epost
        self.fornavn = fornavn
        self.etternavn = etternavn

    def logg_inn(self):
        print(f"{self.epost} logget inn")

    def logg_ut(self):
        print(f"{self.epost} logget ut")

class Lærer(Bruker):
    """ 

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        lønnskonto: Et heltall med brukers lønnskonto
    
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self.lønnskonto = lønnskonto

class Faglærer(Lærer):
    """ 

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        lønnskonto: Et heltall med brukers lønnskonto
    
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.kompetanse = []
        self.klasser = []

class Kontaktlærer(Lærer):
    """ 
    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        lønnskonto: Et heltall med brukers lønnskonto
        klasse: En string med brukers klasse
        trinn: En string med brukers trinn
    
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self._klasse = klasse
        self._trinn = trinn

class Elev(Bruker):
    """ 

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        klasse: En string med brukers klasse
        trinn: En string med brukers trinn
    
    """
    def __init__(self, epost, fornavn, etternavn, klasse, trinn):
        super().__init__(epost, fornavn, etternavn)
        self._klasse = klasse
        self._trinn = trinn
        self._fag = []

# Denne brukesfor testing, betyr at koden bare kjøres hvis vi trykker play på denne fila 
# eller kjører denne fila i terminalen
if __name__ == "__main__": 
    ravi = Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)
    ravi.logg_inn()

    cecilia = Elev("cecc.lemstrom@gmail.com", "Cecilia", "Lemstrøm", "3.klasse", "3STG")
    cecilia.logg_ut()
