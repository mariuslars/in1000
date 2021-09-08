'''
Dette programmet:
- Tar inn navn og bosted og setter sammen til setning med denne informasjonen
- Repeterer x3 i prosedyre
'''

def hent_navn_og_sted():

    navn = input("Skriv inn navn: ")
    sted = input("Skriv in sted: ")

    print(f'Hei, {navn}! Du er fra {sted}')

#Sett antall ganger prosedyren skal kjøres
num_iters = 3
for each_step in range(num_iters):
    hent_navn_og_sted()