"""
Dette programmet:
- Genererer 3 forskjellige motorsykler og øker kilometerstanden til én av dem med 10
"""
from motorsykkel import Motorsykkel

def hovedprogram():

    motorsykkel_1 = Motorsykkel("Volvo", "KH1234", 24)
    motorsykkel_2 = Motorsykkel("Subaru", "DH4321", 43)
    motorsykkel_3 = Motorsykkel("Aprilia", "BR1337", 10)

    

    motorsykkel_1.skrivUt()
    motorsykkel_2.skrivUt()
    motorsykkel_3.skrivUt()

    motorsykkel_3.kjor(10)

    print(motorsykkel_3.hentKilometerstand())

hovedprogram()

