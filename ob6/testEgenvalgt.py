"""
Dette programmet:
- Lar brukeren opprette en variabel om seg selv
- Legge til alle hobbyene sine
"""

from egenvalgt import Person

def hovedprogram():

    navn_input = input("Skriv navnet ditt: ")
    alder_input = input("Skriv alderen din: ")
    hobby_input = input("Skriv inn en hobby: ")

    testPerson = Person(navn_input, alder_input)
    testPerson.leggTilHobby(hobby_input)

    #Ber om flere hobbyer helt til bruker eksplisitt ikke ønsker å legge til flere
    while hobby_input != "9":

        hobby_input = input("Skriv inn en ny hobby eller avslutt ved å skrive '9': ")
        
        #Sørger for at avbryting av legge til hobbyer ikke havner i listen over hobbyer
        if hobby_input != "9":
            testPerson.leggTilHobby(hobby_input)

    testPerson.skrivUt()

hovedprogram()


