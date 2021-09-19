"""
Egenkomponert oppgave:
Skriv et program som legger til og skriver ut venners bursdag
    - Bursdagene skal lagres i en tabell, for eksempel en .txt-fil.
        - Det skal være mulig å skrive til denne tabellen slik at bursdagene blir lagret  
    - Anta at det allerde er to bursdager i tabellen din.
    - La brukeren velge om vedkommende vil hente ut bursdag, legge til bursdag, eller avslutte programmet
"""
def read_bursdager():
    bursdager_dict = open("bursdager.txt")

    read_navn = []
    read_bursdag = []

    for linje in bursdager_dict:
        raw_string = linje.split(",")
        read_navn.append(raw_string[0])
        read_bursdag.append(raw_string[1].rstrip("\n"))
    
    navn_bursdag_list = [read_navn, read_bursdag]

    return navn_bursdag_list

def convert_text_to_dict(navn, bursdag):
    
    bursdager_ordbok = dict(zip(list(navn), list(bursdag)))

    return bursdager_ordbok


def extract_birthday(birthday_dictionary, navn):

    return birthday_dictionary[navn]

def write_to_dict(birthday_dictionary, key, value):
    
    birthday_dictionary[key] = value

def write_to_birthday_table(birthday_dictionary, new_name_input, new_birthday_input):
    
    birthday_dictionary[new_name_input] = new_birthday_input
            
    strings_to_write = []

    #Iterate through all birthday entries in dictionary and format it to correct format for storage in .txt-file.
    for name_write, birthday_write in zip(birthday_dictionary.keys(), birthday_dictionary.values()):
        strings_to_write.append(f'{name_write},{birthday_write}')          

    #Use open with argument "w" to write to file
    #Add \n in write to add new lines
    with open("bursdager.txt", "w") as f:
        for birthday_entry in strings_to_write:
            f.write("%s\n" % birthday_entry)
        f.close()

def run_program():

    bursdager_liste = read_bursdager()

    birthdays = convert_text_to_dict(bursdager_liste[0], bursdager_liste[1])

    current_names_in_dictionary = birthdays.keys()

    active_conditional_outer = True
    while active_conditional_outer:

        print("Velg hva du vil gjøre")
        print("Trykk 0 for å hente bursdag til valgt person")
        print("Trykk 1 for å legge til ny bursdag")
        print("Trykk 9 for å avslutte")

        user_input = input("Velg handling: ")

        if(user_input == "0"):

            active_conditional_inner = True
            
            while active_conditional_inner:
                
                #Skriver informasjon fra listen til bruker
                print("Følgende personer er i listen din: ")
                [print(name) for name in current_names_in_dictionary]
                user_input_name = input("Skriv navnet til vedkommende du ønsker å hente bursdag fra: ")

                if(user_input_name not in current_names_in_dictionary):
                    print("\nDette navnet er ikke tilgjengelig. Prøv igjen\n")
                    continue


                print(f'Bursdagen til {user_input_name} er {birthdays[user_input_name]}')
                active_conditional_outer = active_conditional_inner = False
        
        elif(user_input == "1"):

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

    


run_program()