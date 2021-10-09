"""
Dette programmet:
- Definerer en klasse "Motorsykkel" og metoder for denne
"""

class Motorsykkel:

    def __init__(self, merke, registeringsnummer, kilometerstand):
        self._merke = merke
        self._registeringsnummer = registeringsnummer
        self._kilometerstand = float(kilometerstand)

    # Legger til antall km til Motorsykkel
    def kjor(self, km):

        self._kilometerstand += km

    #Returnerer antall kilometer til Motorsykkel
    def hentKilometerstand(self):

        return(self._kilometerstand)

    #Skriver ut egenskapene til Motorsykkel
    def skrivUt(self):

        print("merke: ",self._merke, 
              "registreringsnummer: ", self._registeringsnummer,
              "kilometerstand: ", self._kilometerstand)



