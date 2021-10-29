## Klasse for representasjon av racks i en regneklynge.
#
class Rack:
    ## oppretter et rack der det senere kan plasseres noder
    #
    def __init__(self):
        self._rackList = []

    ## Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def settInn(self, node):
        
        self._rackList.append(node)

    ## Henter antall noder i racket
    # @return antall noder
    def getAntNoder(self):
        
        numberOfNodes = len(self._rackList)

        return numberOfNodes

    ## Beregner sammenlagt antall prosessorer i nodene i et rack
    # @return antall prosessorer
    def antProsessorer(self):
        
        numProsessorer = 0

        for node in self._rackList:

            numProsessorer += node.antProsessorer()

        return numProsessorer

    ## Beregner antall noder i racket med minne over gitt grense
    # @param paakrevdMinne antall GB minne som kreves
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        
        antallMedNokMinne = 0

        #Itererer over alle noder i rack
        for node in self._rackList:
            
            #Legger til én i antallet med nok minne hvis den består testen
            if node.nokMinne(paakrevdMinne):
                antallMedNokMinne += 1

        return antallMedNokMinne