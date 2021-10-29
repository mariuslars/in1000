from node import Node
from regneklynge import Regneklynge
from rack import Rack
from datasenter import Datasenter

def testFun():
    #############################
    # tester Node-klasse
    node1 = Node(64, 4)
    node2 = Node(128, 8)
    print("tester antProsessorer()")
    assert node1.antProsessorer() == 4, "feilet på antProsessorer()"
    assert node2.antProsessorer() == 8, "feilet på antProsessorer()"



    print("tester nokMinne()")
    assert node1.nokMinne(64) == True, "feillet på nokMinne(64)"
    assert node1.nokMinne(63) == True, "feillet på nokMinne(64)"
    assert node1.nokMinne(65) == False, "feillet på nokMinne(64)"



    #############################
    # tester Rack-klasse

    rack1 = Rack()
    rack2 = Rack()

    rack1.settInn(node1)

    rack2.settInn(node1)
    rack2.settInn(node2)


    print("Tester getAntNoder()")
    assert rack1.getAntNoder() == 1, "Feilet på antall noder == 1"
    assert rack2.getAntNoder() == 2, "Feilet på antall noder == 2"

    print("Tester antProsessorer()")
    assert rack1.antProsessorer() == 4, "Feilet på antProsessorer() == 4"
    assert rack2.antProsessorer() == 12, "Feilet på antProsessorer() == 12"

    print("Tester noderMedNokMinne()")
    assert rack1.noderMedNokMinne(32) == 1, "Feilet på noderMedNokMinne(32) == 1"
    assert rack1.noderMedNokMinne(1337) == 0, "Feilet på noderMedNokMinne(1337) == 0"
    assert rack2.noderMedNokMinne(100) == 1, "Feilet på noderMedNokMinne(100) == 1"
    assert rack2.noderMedNokMinne(10) == 2, "Feilet på noderMedNokMinne(10) == 2"
    assert rack2.noderMedNokMinne(1028) == 0, "Feilet på noderMedNokMinne(1028) == 0"


    #############################
    # tester Regneklynge-klasse

    print("Tester settInnNode()")
    testklynge = Regneklynge(1)
    testklynge2 = Regneklynge(2)

    testklynge.settInnNode(node1)
    testklynge.settInnNode(node2)

    assert testklynge.antProsessorer() == 12, "feilet på antProsessorer() == 12"

    testklynge2.settInnNode(node2)
    testklynge2.settInnNode(node2)
    testklynge2.settInnNode(node2)
    testklynge2.settInnNode(node1)

    assert testklynge2.antProsessorer() == 28, "feilet på antProsessorer() == 28"



    print("Tester noderMedNokMinne() på regneklynge")

    assert testklynge.noderMedNokMinne(2323) == 0, "feilet på noderMedNokMinne(2323) == 0"
    assert testklynge.noderMedNokMinne(0) == 2, "feilet på noderMedNokMinne(0) == 2"
    assert testklynge.noderMedNokMinne(65) == 1, "feilet på noderMedNokMinne(65) == 1"
    assert testklynge2.noderMedNokMinne(65) == 3, "feilet på klynge 2 noderMedNokMinne(65) == 3"


    print("Tester antRacks()")
    assert testklynge.antRacks() == 2, "feilet antRacks == 2"
    assert testklynge2.antRacks() == 2, "feilet antRacks == 2"

    testklynge3 = Regneklynge(3)
    testklynge3.settInnNode(node1)

    assert testklynge3.antRacks() == 1, "feilet antRacks test 3 == 1"

    for i in range(0, 10):
        testklynge3.settInnNode(node1)

    assert testklynge3.antRacks() == 4, "test 4 feilet antRacks  == 4"

    

    testSenter = Datasenter()

    testSenter.lesInnRegneklynge("abel.txt")
    testSenter.lesInnRegneklynge("saga.txt")

    print("skrive ut klynge abel")
    testSenter.skrivUtRegneklynge("abel")

    print("skrive ut alle klynger")
    testSenter.skrivUtAlleRegneklynger()

    print("Alle tester kjørt og bestått")


testFun()