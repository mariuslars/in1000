"""
Dette programmet:
- Lar brukeren planlegge reisen sin
"""

steder = []
klesplagg = []
avreisedatoer = []

#Bruk for å teste program raskere. Sett 5 for å oppfylle krav for oblig
number_of_inputs = 5

for i in range(number_of_inputs):

    steder.append(input("Skriv inn en reisedestinasjon: "))
    klesplagg.append(input("Skriv inn klesplagg for reisen: "))
    avreisedatoer.append(input("Skriv inn dato for reisen: "))

reiseplan = [steder, klesplagg, avreisedatoer]

for destinasjon in reiseplan:
    print(destinasjon)

#For input liste_index1
loop_logical = True
#Get length of sub list to make it more dynamic for testing
len_sublists = number_of_inputs-1
while loop_logical:

    liste_indeks1 = int(input("Velg hvilken liste mellom 0 og 2 du vil hente ut: "))
    if(liste_indeks1 not in range(len(reiseplan))):
        print("Ugyldig input!")
        continue

    loop_logical = False

#For input liste_indeks2
loop_logical = True
while loop_logical:
    
    liste_indeks2 = int(input(f"Velg for vilken destinasjon mellom 0 og {len_sublists} du vil hente ut: "))
    if(liste_indeks2 not in range(len(reiseplan[len_sublists]))):
        print("Ugyldig input!")
        continue
    
    loop_logical = False

print(reiseplan[liste_indeks1][liste_indeks2])