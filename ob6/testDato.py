from dato import Dato

def hovedprogram():

    femtende = Dato(15, 10, 2021)

    print(femtende.lesAar())
    
    if femtende.sammeDato(15):
        print("Loenningsdag!")
    if femtende.sammeDato(1):
        print("Ny maaaned, nye muligheter")

    lesbar_dato = femtende.lagFinDato()
    
    print(lesbar_dato)

    nyDato1 = Dato(15, 11, 2021)
    nyDato2 = Dato(15, 5, 2021)
    nyDato3 = Dato(15, 10, 2021)
    nyDato4 = Dato(16, 10, 2021)
    nyDato5 = Dato(14, 10, 2021)

    gammelString = "gammel dato er: " + femtende.lagFinDato()
    
    print(gammelString)
    print("ny dato er: ", nyDato1.lagFinDato())
    femtende.sjekkRekkefolgeDato(nyDato1)

    print(gammelString)
    print("ny dato er: ", nyDato2.lagFinDato())
    femtende.sjekkRekkefolgeDato(nyDato2)

    print(gammelString)
    print("ny dato er: ", nyDato3.lagFinDato())
    femtende.sjekkRekkefolgeDato(nyDato3)

    print(gammelString)
    print("ny dato er: ", nyDato4.lagFinDato())
    femtende.sjekkRekkefolgeDato(nyDato4)

    print(gammelString)
    print("ny dato er: ", nyDato5.lagFinDato())
    femtende.sjekkRekkefolgeDato(nyDato5)

hovedprogram()
