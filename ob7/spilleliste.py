"""
Dette programmet:
- Etablerer en klasse Spilleliste og metoder for denne
"""
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

        

    #Metode for å lese sanger fra fil og legge til instansevariabelen sanger i spillelisten
    def lesFraFil(self, filnavn):

        #Åpner fil på standard måte
        open_music_file = open(filnavn)

        for line in open_music_file:

            alleData = line.strip().split(";")
            #Legger til Sang objekter i spillelisten
            self._sanger.append(Sang(alleData[1], alleData[0]))

    #Legger til én sang i spillelisten i Spilleliste
    def leggTilSang(self, nySang):

        
        self._sanger.append(nySang)

    #Fjerner første sang som matcher oppgitt sang fra instansevariabel-listen
    def fjernSang(self, sang):

        keep_sang_list = []

        for liste_sang in self._sanger:
            #I stedet for å fjerne sangen som skal ut gjør vi det heller sånn at vi beholder alle andre sanger
            if str(sang) != str(liste_sang):

                keep_sang_list.append(liste_sang)

        self._sanger = keep_sang_list

    #Wrapper for spill i Sang
    def spillSang(self, sang):

        sang.spill()


    #Spill hele spillelistne
    def spillAlle(self):

        for sang in self._sanger:

            sang.spill()

    #Returnerer Sang hvis oppgitt tittel eksisterer    
    def finnSang(self, tittel):

        for sang in self._sanger:
            
            if sang.sjekkTittel(tittel):

                return(sang)

        return None

    #Hent alle sangern til valgt artist
    def hentArtistUtvalg(self, artistnavn):
            
            artist_liste_sanger = []
            for sang in self._sanger:

                if sang.sjekkArtist(artistnavn):

                    artist_liste_sanger.append(sang)

            return artist_liste_sanger


    

