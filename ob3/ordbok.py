"""
Dette programmet:
- Oppretter en ordbok med varenavn og varepriser
- Ber bruker legge til 2 varer med varenavn og varepriser
"""

#Definerer ordboken og legger til varenavn- og varepriserliste
varer = {"varenavn": [], "varepriser": []}
varenavn =  ["melk", "brod", "yoghurt", "pizza"]
varepriser = [14.9, 24.9, 12.9, 39.9]

varer["varenavn"] = varenavn
varer["varepriser"] = varepriser

print(varer)

#Sett antall varer og varepriser bruker skal legge til i ordboken
antall_nye_varer = 2

#Tomme lister som skal fylles med brukers input for hver iterasjon
nye_varer = []
nye_priser = []
for i in range(antall_nye_varer):
    nye_varer.append(input("Legg ny vare til ordboken: "))
    nye_priser.append(float(input("Legg til pris for varen: ")))

#Bruker extend siden 2 lister skal concateneres
varer["varenavn"].extend(nye_varer)
varer["varepriser"].extend(nye_priser)

print(varer)