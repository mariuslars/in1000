from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def __str__(self):

        song_unpack = '|'.join([song[0]+";"+song[1] for song in self._sanger])
        return song_unpack


    def lesFraFil(self, filnavn):

        open_music_file = open(filnavn)

        for line in open_music_file:

            alleData = line.strip().split(";")
            self._sanger.append(alleData)

    def leggTilSang(self, nySang):

        
        nySang_entry = str(nySang).split(";")
        self._sanger.append(nySang_entry)

    def fjernSang(self, sang):
        [liste_sang for liste_sang in self._sanger if sang not in liste_sang]

    def finnSang(self, tittel):

        for sang in self._sanger:

            if tittel.lower() == sang[0].lower():

                return(sang)

        return None

tester = Spilleliste("Listenavn")
tester.lesFraFil("musikk.txt")

print(tester)
sang1 = Sang("Bon Iver", "The Great River")
tester.leggTilSang(sang1)

print(tester)
funnet_sang = tester.finnSang("GoiNG for the one")
print("dette re funnet sang: ",funnet_sang)

tester.fjernSang(funnet_sang)

print(tester)

print(tester._sanger)