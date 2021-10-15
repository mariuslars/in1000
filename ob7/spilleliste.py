from sang import Sang

class Spilleliste:

    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def __str__(self):
        #Definerer str-metode mest for å kunne enkelt sjekke innholdet i objektet
        sang_str_liste = []
        for song in self._sanger:
            #Benytter det faktum at vi har definert __str__-metode tidligere for enklere å parse sangen
            sang_str_liste.append(str(song))

        #Litt tilfeldig valg av print her. Men benytter | for å enkelt kunne splitte i fremtiden
        return '|'.join(sang_str_liste)

        


    def lesFraFil(self, filnavn):

        #Åpner fil på standard måte
        open_music_file = open(filnavn)

        for line in open_music_file:

            alleData = line.strip().split(";")
            #Legger til Sang objekter i spillelisten
            self._sanger.append(Sang(alleData[1], alleData[0]))

    def leggTilSang(self, nySang):

        
        self._sanger.append(nySang)

    def fjernSang(self, sang):

        keep_sang_list = []

        for liste_sang in self._sanger:
            #I stedet for å fjerne sangen som skal ut gjør vi det heller sånn at vi beholder alle andre sanger
            if str(sang) != str(liste_sang):

                keep_sang_list.append(liste_sang)

        self._sanger = keep_sang_list

    def spillSang(self, sang):

        
        sang.spill()

    def spillAlle(self):

        for sang in self._sanger:

            sang.spill()

    
    def finnSang(self, tittel):

        for sang in self._sanger:
            
            if sang.sjekkTittel(tittel):

                return(str(sang))

        return None


    def hentArtistUtvalg(self, artistnavn):
            
            artist_liste_sanger = []
            for sang in self._sanger:

                if sang.sjekkArtist(artistnavn):

                    artist_liste_sanger.append(str(sang))

            return artist_liste_sanger


    

tester = Spilleliste("Listenavn")
tester.lesFraFil("musikk.txt")



print("Print object: ")
print(tester)

sang1 = Sang("Bon Iver", "The Great River")
tester.leggTilSang(sang1)

print("Printer etter å ha lagt til sang: ")
print(tester)


print("-----------------------------------------------")
print("Printer resultat av sang som ikke er funnet: ")
funnet_sang_ikke = tester.finnSang("GoiNG for the oned")

print(funnet_sang_ikke)
funnet_sang = tester.finnSang("GoiNG for the one")
print("Dette er sang som er funnet: ",funnet_sang)

print("Fjerner sangen over: ")
tester.fjernSang(funnet_sang)

print(tester)

tester.spillAlle()
print(Sang("Queen of", "LOL").sjekkArtist("qudeen of d"))
print(tester.hentArtistUtvalg("iver"))