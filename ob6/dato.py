"""
Dette programmet:
- Definerer klassen Dato og metoder for denne
"""

class Dato:

    def __init__(self, nyDag, nyMaaned, nyttAar):

        self._dag = int(nyDag)
        self._maaned = int(nyMaaned)
        self._aar = int(nyttAar)

    #Metode som returnerer årstall fra Dato
    def lesAar(self):

        return(self._aar)

    def lagFinDato(self):

        maaneder = {1: "januar",
                    2: "februar",
                    3: "mars", 
                    4: "april",
                    5: "mai",
                    6: "juni",
                    7: "juli",
                    8: "august",
                    9: "september",
                    10: "oktober",
                    11: "november",
                    12: "desember"}

        return(f'{self._dag}. {maaneder[self._maaned]} {self._aar}')

    def sammeDato(self, dag):

        is_day = self._dag == dag

        return(is_day)


    #Metode for å sjekke hvilken av objektet og ny dato som kommer først.
    #
    def sjekkRekkefolgeDato(self, ny_dato):

        etterString = "Ny dato kommer etter eksisterende dato"
        forString = "Ny dato kommer før eksisterende dato"
        sammeString = "Ny dato er lik som eksisterende dato"

        if self._aar > ny_dato._aar:
            print(forString)
        elif self._aar < ny_dato._aar:
            print(etterString)
        else:

            if self._maaned > ny_dato._maaned:
                print(forString)
            elif self._maaned < ny_dato._maaned:
                print(etterString)
            else:

                if self._dag > ny_dato._dag:
                    print(forString)
                elif self._dag < ny_dato._dag:
                    print(etterString)
                else:
                    print(sammeString)
