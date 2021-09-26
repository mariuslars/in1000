"""
Dette programmet:
- definerer en funksjon som henter inn mål fra ,.txt
- Regner ut en liste av tommer til cm
"""

def get_maal():
    opened_file = open("maal_skredder.txt")

    body_ordbok = {}

    for line in opened_file:
        body_location, body_measure = line.split()
        
        body_ordbok[body_location] = body_measure

    return(body_ordbok)



def tommerTilCm(antallTommer):

    assert antallTommer > 0, "antallTommer må være større enn 0"

    return antallTommer * 2.54

def evaluerListe(liste_maal):

    for maal in liste_maal:

        print(f'{maal} tommer er {tommerTilCm(maal)} cm')

testliste = [12.3, 12, 9, 0.1]

evaluerListe(testliste)