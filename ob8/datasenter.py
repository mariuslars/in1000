## Klasse for representasjon av et datasenter
#
from node import Node
from regneklynge import Regneklynge


class Datasenter:

    ## Oppretter et datasenter
    #
    def __init__(self):
        self._datasenterDict = {}

    ## Leser inn data om en regneklynge fra fil og legger
    # den til i ordboken
    # @param filnavn filene der dataene for regneklyngen ligger
    def lesInnRegneklynge(self, filnavn):

        #Fjerner de siste 4 characters i filnavn-string (.txt) og bruker dette som key
        dictKey = filnavn[0:-4]

        #Legger filen i minne og gjør klar for å hente ut informasjon
        aapneRegneklynge = open(filnavn)

        storeLines = []
        for line in aapneRegneklynge:
            storeLines.append(line.strip())
        
        #Første element i storeLines er max noder per rack
        maxNoder = storeLines[0]

        #Andre og tredje element i storeLines er AntallNoder MinnePerNode AntallprosessorerPerNode
        AntallNoder1, MinnePerNode1, AntallprosessorerPerNode1 = storeLines[1].split(" ")
        AntallNoder2, MinnePerNode2, AntallprosessorerPerNode2 = storeLines[2].split(" ")

        #Oppretter key-value pair i ordbok med Regneklynge
        self._datasenterDict[dictKey] = Regneklynge(maxNoder)

        #Oppretter de to forskjellig type nodene
        node1 = Node(MinnePerNode1, AntallprosessorerPerNode1)
        node2 = Node(MinnePerNode2, AntallprosessorerPerNode2)

        #Genererer alle noder spesifisert fra .txt-filen som er lest
        #og legger de til i datasenteret
        for iter in range(0, int(AntallNoder1)):
            self._datasenterDict[dictKey].settInnNode(node1)

        for iter in range(0, int(AntallNoder2)):
            self._datasenterDict[dictKey].settInnNode(node2)


    ## Skriver ut informasjon om alle regneklyngene
    #
    def skrivUtAlleRegneklynger(self): 
        
        for regneklynge in self._datasenterDict:
            print("\nInformasjon om regneklyngen", regneklynge, "\n")
            self.skrivUtRegneklynge(regneklynge)

    ## Skriver ut informasjon om en spesifikk regeklynge
    # @param navn navnet på regnekyngen
    def skrivUtRegneklynge(self, navn):
        antallProsessorer = self._datasenterDict[navn].antProsessorer()
        antallRack = self._datasenterDict[navn].antRacks()
        antallNoder32 = self._datasenterDict[navn].noderMedNokMinne(32)
        antallNoder64 = self._datasenterDict[navn].noderMedNokMinne(64)
        antallNoder128 = self._datasenterDict[navn].noderMedNokMinne(128)

        print("Noder med minst 32 GB: ", antallNoder32)
        print("Noder med minst 64 GB: ", antallNoder64)
        print("Noder med minst 128 GB: ", antallNoder128)
        print("Antall prosessorer: ", antallProsessorer)
        print("Antall rack: ", antallRack)