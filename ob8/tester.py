from node import Node
from rack import Rack
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
print("Alle tester kjørt")