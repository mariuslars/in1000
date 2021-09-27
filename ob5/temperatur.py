"""
1.)
"""

def read_max_temperatures(file_path):
    opened_file = open(file_path)

    lines_months = []
    lines_temperatures = []

    for line in opened_file:
        raw_string = line.split(",")
        lines_months.append(raw_string[0])
        #Husk å fjerne tegnet for newline som blir lest inn
        lines_temperatures.append(float(raw_string[1].rstrip("\n")))
        
    file_dictionary = dict(zip(lines_months, lines_temperatures))

    return(file_dictionary)

max_temperatures = read_max_temperatures("max_temperatures_per_month.csv")
print(max_temperatures)
"""
#2.)
"""
def evaluate_maximum(max_dictionary, file_path):

    opened_file = open(file_path)

    for line in opened_file:
        list_strings = line.split(",")
        month = list_strings[0]
        day = list_strings[1]
        temperature = float(list_strings[2])
        max_current_month = max_dictionary[month]

        if(max_current_month < temperature):
            print(f'Ny varmerekort på {day}. {month}: {temperature}. (gammel varmerekord var {max_current_month})')
            """
            3.)
            """
            max_dictionary[month] = temperature
    
evaluate_maximum(max_temperatures, "max_daily_temperature_2018.csv")


"""
5.)
"""

def findHeatWave():
    temperature_file = open("max_daily_temperature_2018.csv")

    #Starter teller for å ha kontroll på hvor langt vi har kommet slik at vi kan gå "en tilbake" for å hente ut siste dag av heatwave 
    iterator_counter = 0
    #Starter teller for å telle antall dager temperaturen er over 25 
    heatwave_counter = 0
    #Lager en liste med dager for å kunne gå "en tilbake" hvis vi har kommet til slutten på heatwave
    list_of_days = []

    for line in temperature_file:
       
        month, day, temperature_string = file_entries_list = line.split(",")
        temperature = float(temperature_string)
        list_of_days.append(f'{day}. {month}')

        #Vi sjekker om temperaturen er over 25. Da vil telleren øke med én. 
        #I øyeblikket vi får en observasjon på 25 eller lavere evaluerer vi hvor mange dager hetebølgen har vart basert på tellingene i heatwave_counter
        #Hvis det er 5 eller flere henter vi ut hvilken dag som "var i går", og rapporterer denne som siste.
        #Første dag i heatwave er når heatwave_counter == 1, altså første gang en observasjon er over 25
        if(temperature > 25):
            heatwave_counter += 1
            if(heatwave_counter == 1):
                first_heatwave_day = list_of_days[iterator_counter]
        else:
            if(heatwave_counter >= 5):
                final_heatwave_day = list_of_days[iterator_counter-1]
                
                print(f'Hetebølgen startet {first_heatwave_day} og hadde siste dag {final_heatwave_day}')

                #Resetter teller fordi vi har funnet en hetebølge som er avsluttet, og leter nå etter ny hetebølge
                heatwave_counter = 0
            else:
                #Avslutter teller fordi vi har hatt observasjoner over 25, men antall under 5. Nå leter vi etter ny hetebølge
                heatwave_counter = 0

        iterator_counter += 1
        

findHeatWave()


""" 
def write_max_temperatures:


    with open("max_temperatures_per_month_updated.csv", "w") as updated_max_temps:
        for temperature_entry in temperature_strings_to_write:
            updated_max_temps.write("%s\n" % temperature_entry)
        updated_max_temps.close() 
"""

