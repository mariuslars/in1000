"""
Dette programmet:
- Definerer en ordbok med matplan for brukere
- Definerer og kjører en prosedyre som henter ut informasjon om matplan for valgt bruker
"""

matplan_dict = {"Marius": ["frokost: brød", "lunsj: egg", "middag: pølser"],
                "Lars": ["Frokost: havregryn", "lunsj: brød", "middag: pizza"]}

#Lagrer navn i en liste for å enklere sjekke brukerinput mot navn i matplan i prosedyren
matplan_navn = [key for key in matplan_dict.keys()]


def get_matplan_by_navn():

    #Concat navnene i listen for å kunne concate med string senere
    #Separerer list entries med ", "
    concatenated_matplan_navn = ", ".join(matplan_navn)
    print("Navn på alle beboere: "+ concatenated_matplan_navn)

    input_navn = input("Skriv inn navn på beboer: ")

    #Sjekker om navnet som er oppgitt av bruker eksisterer i matplanen
    is_input_navn_in_matplan = input_navn in matplan_navn

    if(not is_input_navn_in_matplan):
        print("Denne brukeren er ikke registrert")
    else:
        print(matplan_dict[input_navn])

get_matplan_by_navn()
    


#Oppgave 3:
#a) 
""" 
Brukernavn på alle IN1000 studenter passer i mengde siden det ikke er mulig med duplikater. Alle har unikt brukernavn
"""
#b)
"""
Brukernavn og antall poeng passer i ordbok siden dette er key:value pairs, noe ordbok støtter (brukernavn = key, poeng =) value
"""
#c)
"""
Alle vinnere i Lotto kan ha dupliserte navn, derfor kan man ikke bruke mengde. Liste kan egne seg for dette
"""
#d)
""" 
Kan defineres som et key:value-pair, spesielt hvis gjestene blir servert mat individuelt og ikke i buffet. Da vil gjest = key, allergener = values, eventuelt en nested med bordnummer ytterst.
Hvis buffet kan det defineres som liste siden duplikater burde tillates slik at man kan vurdere mengde (antall/vekt, ikke "set") med mat man må forberede for de med allergier. Mengder vil obscure denne informasjonen.
"""
