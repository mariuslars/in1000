"""
Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter
og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
instansvariabel hobbyer som en tom liste . Skriv en metode leggTilHobby som tar
imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode
skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og
alder kaller på metoden skrivHobbyer.
Lag deretter et testprogram for klassen Person der du lar brukeren skrive inn navn og
alder, og oppretter et Person-objekt med informasjonen du får. Deretter skal brukeren
ved hjelp av en løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger
ønsker å oppgi hobbyer skal informasjon om brukeren skrives ut.

Dette programmet:
- Definerer en klasse Person og metoder for denne
"""

class Person:

    def __init__(self, navn, alder):
        
        self._navn = navn
        self._alder = alder
        self._hobbyer = []


    def leggTilHobby(self, hobby):

        self._hobbyer.append(hobby)
    
    def skrivHobbyer(self):

        hobby_linje = ', '.join(self._hobbyer)
        print(hobby_linje)

    def skrivUt(self):
        
        print("Navn: ", self._navn)
        print("Alder: ", self._alder)
        self.skrivHobbyer()


