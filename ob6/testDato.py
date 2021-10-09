from dato import Dato

def hovedprogram():

    femtende = Dato(5, 10, 2022)

    print(femtende.lesAar())
    
    if femtende.sammeDato(15):
        print("Loenningsdag!")
    if femtende.sammeDato(1):
        print("Ny maaaned, nye muligheter")

    lesbar_dato = femtende.lagFinDato()
    
    print(lesbar_dato)

    nyDato = Dato(15, 10, 2023)

    femtende.sjekkRekkefolgeDato(nyDato)

hovedprogram()
