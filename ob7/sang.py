"""
Dette programmet:
- Definerer klassen Sang og metoder for denne
"""
class Sang:

    def __init__(self, artist, tittel):
        
        self._artist = artist
        self._tittel = tittel

    def __str__(self):

        return f'{self._tittel};{self._artist}'

    #Metode for å generere output ved avspilling
    def spill(self):

        print(f"Spiller {self._tittel} av {self._artist}")

    #Metode for å se om oppgitt artistnavn er samme som i instansevariabelen
    #Trenger kun match på ett ord i navnet.
    def sjekkArtist(self, navn):
        #Splitter opp og lager sett siden det holder med partial match på ett eller flere ord
        artist_split = self._artist.lower().split(" ")
        artistnavn_split = navn.lower().split(" ")

        artist_set = set(artist_split)
        artistnavn_set = set(artistnavn_split)

        #Finner intersection av settene for å senere vurdere lengden. 
        #Hvis intersection er 0 er det ingen match
        artist_intersection = artist_set.intersection(artistnavn_set)

        #Conditional for setlengden
        set_is_not_empty = len(artist_intersection) > 0

        if set_is_not_empty:

            return True

        else: 

            return False

    #Metode for å se om oppgitt tittel er den samme som i instansevariabelen
    def sjekkTittel(self, tittel):

        if tittel.lower() == self._tittel.lower():

            return True
        else:

            return False

    def sjekkArtistOgTittel(self, artist, tittel):
        
        #Begge må være sanne for at vi skal returnere True.
        both_are_true = self.sjekkArtist(artist) & self.sjekkTittel(tittel)

        if both_are_true:
            
            return True
        
        else:

            return False
        


