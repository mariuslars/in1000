class Sang:

    def __init__(self, artist, tittel):
        self._artist = artist
        self._tittel = tittel

    def spill(self):

        print(f"Spiller {self._tittel} av {self._artist}")

    def sjekkArtist(self, navn):

        artist_split = self._artist.lower().split(" ")

        if navn.lower() in artist_split:

            return True

        else: 

            return False

    def sjekkTittel(self, tittel):

        if tittel.lower() == self._tittel.lower():

            return True
        else:

            return False

    def sjekkArtistOgTittel(self, artist, tittel):

        both_are_true = self.sjekkArtist(artist) & self.sjekkTittel(tittel)

        if both_are_true:
            
            return True
        
        else:

            return False
        
    def __str__(self):

        return f'{self._tittel};{self._artist}'


""" sang1 = Sang("Prince of arabia", "night of the storm")

sang1.spill()

print(sang1.sjekkArtist("LOL"))
print(sang1.sjekkArtist("PRINCe"))

print(sang1.sjekkTittel("night of the storM"))
print(sang1.sjekkTittel("NIGHT of THE storM"))
print(sang1.sjekkTittel("night of the storm"))
print(sang1.sjekkTittel("night of the stor"))

print("SjekkArtigstOgTittelStarter her")
print(sang1.sjekkArtistOgTittel("PRinCe", "NiGHt of the storm"))

print(sang1.sjekkArtistOgTittel("PRinCe", "NiGHt of the stormd"))
print(sang1.sjekkArtistOgTittel("PRinCed", "NiGHt of the storm"))
print(sang1.sjekkArtistOgTittel("PRinCedasd", "NiGHt of the stormasd"))

print(sang1)
print(str(sang1))
 """