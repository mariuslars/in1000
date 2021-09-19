"""
Egenkomponert oppgave:
Skriv et program som kan legge til og hente ut venners bursdag
    - Bursdagene skal lagres i en tabell, for eksempel en .txt-fil.
        - Det skal være mulig å skrive til denne tabellen slik at bursdagene blir lagret
        - Formatet på tabellen og strukturen på bursdagene er valgfritt
    - Anta at det allerde er to bursdager i tabellen din.
    - La brukeren velge om vedkommende vil hente ut bursdag, legge til bursdag, eller avslutte programmet
"""
def read_birthdays():
    #Henter tabellen fra disk inn i minnet
    #Konverterer tabellen til en liste med lister hvor navn og bursdager er i hver sin liste
    bursdager_dict = open("bursdager.txt")

    read_navn = []
    read_bursdag = []

    for linje in bursdager_dict:
        raw_string = linje.split(",")
        read_navn.append(raw_string[0])
        read_bursdag.append(raw_string[1].rstrip("\n"))
    
    navn_bursdag_list = [read_navn, read_bursdag]

    return navn_bursdag_list

def convert_text_to_dict(key_name, value_bursdag):
    #Converterer to lister til en ordbok i key-value format

    bursdager_ordbok = dict(zip(list(key_name), list(value_bursdag)))

    return bursdager_ordbok


def extract_birthday(birthday_dictionary, navn):
    #Henter ut value fra ordbok

    return birthday_dictionary[navn]

def write_to_birthday_table(birthday_dictionary, new_name_input, new_birthday_input):
    #Åpner og skriver alle bursdager i ordboken til tabellen/.txt-filen.
    #TODO: Skriv kun entries som allerede ikke er i ordboken
    
    birthday_dictionary[new_name_input] = new_birthday_input
            
    strings_to_write = []

    #Iterate through all birthday entries in dictionary and format it to correct format for storage in .txt-file.
    for name_write, birthday_write in zip(birthday_dictionary.keys(), birthday_dictionary.values()):
        strings_to_write.append(f'{name_write},{birthday_write}')          

    #Use open with argument "w" to write to file
    #Add \n in write to add new lines
    with open("bursdager.txt", "w") as birthday_file:
        for birthday_entry in strings_to_write:
            birthday_file.write("%s\n" % birthday_entry)
        birthday_file.close()

def manage_birthdays():

    #Leser tabellen fra disk inn i minnet
    bursdager_liste = read_birthdays()

    #Genrerer bursdagsordboken
    birthdays = convert_text_to_dict(bursdager_liste[0], bursdager_liste[1])

    names_in_dictionary = birthdays.keys()

    #Run condition for while loop
    active_conditional_outer = True

    while active_conditional_outer:

        print("Velg hva du vil gjøre")
        print("Trykk 0 for å hente bursdag til valgt person")
        print("Trykk 1 for å legge til ny bursdag")
        print("Trykk 9 for å avslutte")

        user_input = input("Velg handling: ")

        if(user_input == "0"):
            #Bruker ønsker å hente ut bursdag fra valg person

            #Run condition for while loop
            active_conditional_inner = True
            
            #Ekstra inner while i tilfelle bruker skriver inn et navn som ikke er i oversikten
            while active_conditional_inner:
                
                #Skriver informasjon fra listen til bruker
                print("Følgende personer er i listen din: ")
                [print(name) for name in names_in_dictionary]
                user_input_name = input("Skriv navnet til vedkommende du ønsker å hente bursdag fra: ")

                if(user_input_name not in names_in_dictionary):
                    print("\nDette navnet er ikke tilgjengelig. Prøv igjen\n")
                    continue


                print(f'Bursdagen til {user_input_name} er {birthdays[user_input_name]}')
                active_conditional_outer = active_conditional_inner = False
        
        elif(user_input == "1"):
            #Hvis bruker ønsker å legge til bursdag i oversikten
            new_name = input("Skriv navnet til personen du ønsker å legge til: ")
            new_birthday = input("Skriv bursdagen til personen: ")

            write_to_birthday_table(birthdays, new_name, new_birthday)

            print(f"Du har lagt til {new_name} med bursdag {birthdays[new_name]} i ordboken din")

            active_conditional_outer = False

        elif(user_input == "9"):
            print("Den er grei")
            active_conditional_outer = False
        
        
        else:
            print("Ikke et godkjent valg. Prøv på nytt")
            continue

    


manage_birthdays()