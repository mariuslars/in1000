
"""
Dette programmet:
- Definerer en prosedyre som tar en alder og returnerer en billettpris basert på regler
"""

def billettpris_gitt_alder():

    alder = int(input("Skriv inn alder på kjøperen: "))
    billettpris = 0

    if(alder <= 17):
        billettpris = 30
    elif(alder > 17 and alder < 63):
        billettpris = 50
    else:
        billettpris = 35
    
    print(f"Billettprisen din er {billettpris} kroner")

billettpris_gitt_alder()

"""
Prosedyren virker tilsynelatende som den skal. 
- 15 returnerer 30kr, 
- 31 returnerer 50kr,
- 63 returnerer 35kr
Ser ikke noe galt
"""