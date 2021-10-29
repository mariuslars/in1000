from datasenter import Datasenter

def hovedprogram():

    hovedDataSenter = Datasenter()


    hovedDataSenter.lesInnRegneklynge("abel.txt")
    hovedDataSenter.lesInnRegneklynge("saga.txt")

    hovedDataSenter.skrivUtAlleRegneklynger()

hovedprogram()