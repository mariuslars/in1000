## Klasse for representasjon av regneklynge med racks og noder
# 
from rack import Rack


class Regneklynge:
	## Oppretter en regneklynge og setter maks antall
	# det er plass til i et rack
	# @param noderPerRack max antall noder per rack
    def __init__(self, noderPerRack):
        self._regneklyngeListe = []
        self._maksNoder = int(noderPerRack)


    ## Plasserer en node inn i et rack med ledig plass, eller i et nytt
    # @param node referanse til noden som skal settes inn i datastrukturen
    def settInnNode(self, node):
        
        klyngeLengde = len(self._regneklyngeListe)

        #Hvis regneklyngen ikke inneholder noen Racks må vi legge til én Rack
        #Kan ansees som init av regneklynge
        if klyngeLengde == 0:
            init_rack = Rack()
            self._regneklyngeListe.append(init_rack)
        
        #Vi henter ut den siste racken i regneklyngen for å se om den er på max antall noder
        sisteRack = self._regneklyngeListe[-1]
        #Hent ut antall noder i den siste racken
        antSisteRack = sisteRack.getAntNoder()
        
        #Hvis siste rack har antall noder lavere enn max kan vi legge til nodene her
        if antSisteRack < self._maksNoder:
            #Setter inn noden i siste Rack
            self._regneklyngeListe[-1].settInn(node)

        else:
            
            #Hvis siste Rack ikke har færre antall noder enn maksNoder må vi sette inn nytt Rack
            #Etablerer tomt nytt rack
            nyttRack = Rack()
            #Legger nytt rack med node inn i regneklyngen. append legger automatisk til sist
            self._regneklyngeListe.append(nyttRack)
            #Setter inn noden i siste Rack
            self._regneklyngeListe[-1].settInn(node)
            






    ## Beregner totalt antall prosessorer i hele regneklyngen
    # @return totalt antall prosessorer
    def antProsessorer(self):
        
        prosessorCounter = 0

        #Itererer gjennom Racks in regneklyngen og summerer opp alle prosessorer
        for rack in self._regneklyngeListe:
            prosessorCounter += rack.antProsessorer()

        return prosessorCounter

    ## Beregner antall noder i regneklyngen med minne over angitt grense
    # @param paakrevdMinne hvor mye minne skal noder som telles med ha
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):

        noderMedNokMinneCounter = 0

        for rack in self._regneklyngeListe:

            noderMedNokMinneCounter += rack.noderMedNokMinne(paakrevdMinne)

        return noderMedNokMinneCounter

    ## Henter antall racks i regneklyngen
    # @return antall racks
    def antRacks(self):
        
        antallRacks = len(self._regneklyngeListe)

        return antallRacks
