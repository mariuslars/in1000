"""
Først defineres funksjonen minFunksjon uten argumenter. Deretter defineres prosedyren hovedprogram uten argumenter. Deretter kalles hovedprogram.
hovedprogrammet oppretter variabel a med verdi 42 og b med verdi 0, for deretter å printe ut verdien til variabelen b. b settes deretter lik a, og begge har nå en verdi på 42.
Deretter kalles funksjonen minFuksjon som itererer over [0, 1]. Her opprettes en variabel c med verdi 2, som deretter blir printet ut. Så legger vi til 1 til c, som nå har en verdi på 3
Deretter opprettes en ny variabel b med verdi 10, før b blir forsøkt lagt til verdi fra a. Her vil programmet stoppe siden a ikke er definert i funksjonen.
"""

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)
def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)
hovedprogram()