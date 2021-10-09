"""
Dette programmet:
- Definerer en klasse Hund og dens metoder
"""

class Hund:

    def __init__(self, alder, vekt):

        self._alder = int(alder)
        self._vekt = float(vekt)
        self._metthet = 10

    #Metode som returnerer vekten til Hund
    def hentVekt(self):

        return(self._vekt)

    #Metoden som returnerer alder til Hund
    def hentAlder(self):

        return(self._alder)

    #Metode som lar Hund springe
    def spring(self):

        self._metthet -= 1

        if self._metthet < 5:

            self._vekt -= 1
    
    #Metode som lar hund spise
    def spis(self, mengde):

        self._metthet += int(mengde)
        
        if self._metthet > 7:

            self._vekt += 1

