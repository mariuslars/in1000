"""
Dette programmet:
- Definerer en funksjon som summerer to integers
- Printer resultatet av to vilkårlig valgte sett med to integers
"""

#1.
def adder(tall1, tall2):

    total = tall1 + tall2

    return total

list_integers = [[1, 2], [20, 21]]

for tall in list_integers:

    add_result = adder(tall[0], tall[1])
    print(tall[0], "+", tall[1], "=", add_result)
    
#2., 3. 

def tellForekomst(minTekst, minBokstav):

    #Initiate letter counter. Will increase by one each time the letter is in the sentence
    point_counter = 0
    for letter in range(len(minTekst)):

    #Hvis den oppgitte bokstaven er i strengen, pluss på én i counter
        if(minBokstav in minTekst[letter]):
            point_counter += 1
    
    return point_counter



input_string = input("Skriv inn en tekst: ")
input_letter = input("Skriv inn én bokstav: ")

required_letter_length = 1

#Er dette litt for voldsomt å kaste error for? Burde man heller ha en while loop som går så lenge len(input_letter) != 1?
#assert len(input_letter) == required_letter_length, "antall bokstaver er for mange. Skriv kun én bokstav"

antall_forekomster = tellForekomst(input_string, input_letter)
    
print(f"I tekststrengen '{input_string}' forekommer bokstaven '{input_letter}' {antall_forekomster} ganger")
