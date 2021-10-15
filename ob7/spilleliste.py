from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def __str__(self):

        song_unpack = '|'.join([song for song in self._sanger])
        return song_unpack


    def lesFraFil(self, filnavn):

        open_music_file = open(filnavn)

        for line in open_music_file:

            alleData = line.strip()#.split(";")
            self._sanger.append(alleData)

    def leggTilSang(self, nySang):

        
        nySang_entry = str(nySang)#.split(";")
        self._sanger.append(nySang_entry)

    def fjernSang(self, sang):
        self._sanger = [liste_sang for liste_sang in self._sanger if sang not in liste_sang]


    def spillAlle(self):

        for sang in self._sanger:

            print(f"Spiller av: {sang}")

    
    def finnSang(self, tittel):

        for sang in self._sanger:
            splitta_sang = sang.split(";")
            if tittel.lower() == splitta_sang[0].lower():

                return(sang)

        return None

    def hentArtistUtvalg(self, artistnavn):
            print()

    

tester = Spilleliste("Listenavn")
tester.lesFraFil("musikk.txt")

print("Print object: ")
print(tester)

sang1 = Sang("Bon Iver", "The Great River")
tester.leggTilSang(sang1)

print("Printer etter å ha lagt til sang: ")
print(tester)

funnet_sang_ikke = tester.finnSang("GoiNG for the onasddase")
print("Printer resultat av sang som ikke er funnet: ")
print(funnet_sang_ikke)
funnet_sang = tester.finnSang("GoiNG for the one")
print("Dette er sang som er funnet: ",funnet_sang)

print("Fjerner sangen over: ")
tester.fjernSang(funnet_sang)

print(tester)

tester.spillAlle()