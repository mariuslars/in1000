"""  
Skriv oppgavetekst til en oppgave som handler om lister eller ordbøker. Et forslag
kan være å skrive en quiz som i forrige uke, men ved å bruke lister. Alternativt et
program som sjekker alle allergier (for eksempel for deltakere ved påmelding til et
arrangement), og skriver ut en oversikt til slutt over hva slags mat som bør unngås.
2. Løs oppgaven! Du skal levere både oppgaveteksten og besvarelsen (skriv
oppgaveteksten som kommentarer over løsningen din).
"""

""" 
Oppgavetekst
- Skriv et program som lar en bruker hente ingredienser til forskjellige matretter
    - Skriv ut en oversikt over tilgjengelige matretter
    - La deretter bruker skrive in ønsket matrett for deretter å returnere antall ingredienser
    - Hvis bruker oppgir en matrett som ikke eksisterer i ordbok, be de skrive inn på nytt helt til de velger en matrett som er i ordboken.
"""

matretter_dict = {"Pizzadeig": ["Gjær", "Salt", "Hvetemel", "Vann", "Olje"],
                  "Lapskaus": ["Smør", "Høyrygg av storfe", "Vann", "Kjøttbuljong", "Gulrot", "Kålrot", "Persillerot", "Purre", "Salt", "Pepper"],
                  "Pastasaus": ["Tomat", "Kjøttdeig", "Gulrot", "Stangseleri", "Løk", "Rødvin", "Olje", "Hvitløk", "Kjøttbuljong", "Laurbærblad", "Salt", "Pepper"]}

matretter_list = [key for key in matretter_dict.keys()]

def get_ingredienser(counter):

    if(counter == 1):
        print("Tilgjengelige matretter: \n" + "\n".join(matretter_list))
    
    ingrediens_input = input("Hvilken matrett ønsker du ingrediensene for? ")

    ingrediens_is_in_matretter = ingrediens_input in matretter_list

    if(ingrediens_is_in_matretter):
        print(matretter_dict[ingrediens_input])
        return(True)
        
    else:
        print("Matrett er ikke tilgjengelig. Prøv igjen")
        return(False)


#Be de skrive inn helt til de treffer en matrett som er i ordboken
iter_num = 1
dec = False
while dec == False:
    dec = get_ingredienser(counter = iter_num)
    iter_num += 1
