"""
Dette programmet:
- Simulerer en hund som springer mer enn den spiser og derfor går ned i vekt. 
"""
from hund import Hund

def hovedprogram():

    tassen = Hund(10, 134)


    print("startvekt: ", tassen.hentVekt())
    [tassen.spring() for i in range(0, 10)]
    print("Vekt etter 10 løp",tassen.hentVekt())
    tassen.spis(20)
    print("Vekt etter å ha spist 20: ",tassen.hentVekt())
    [tassen.spring() for i in range(0, 40)]
    print("Vekt etter 20 løp: ",tassen.hentVekt())
    tassen.spis(10)
    print("Vekt etter å ha spist 10: ",tassen.hentVekt())
    
    
hovedprogram()



