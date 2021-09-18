"""
Dette programmet:

"""

#1.), 2.)
#Definerer tom liste som skal inneholde alle bruker-inputs
user_input_list = []
while 0 not in user_input_list:

    user_input = input("Skriv et tall. Avslutt med '0': ")

    #try-except for at den ikke skal feile på string. Tillater float siden det er spesifisert "tall" i oppgavetekst, ikke kun integer
    try:
        float(user_input)
    except:
        print("Ikke et tall. Prøv igjen")
        continue


    user_input_list.append(float(user_input))

#Fjerner siste tall (som alltid er 0) så det ikke påvirker videre beregninger
user_input_list = user_input_list[:-1]
#3.)
for item in user_input_list:
    print(item)

#4.)

#Definer variabelen som skal summere opp listen
minSum = 0
for item in user_input_list:
    minSum += item

print("Sum av dine tall er ", minSum)

#5.)


#minimum_value må inneholde en initiell verdi for å kunne evalueres mot de andre i listen.
#Kan ikke initieres med '0' da dette vil påvirke hva som blir minimum hvis bruker taster inn tall i intervallet (0, Inf)
#Følgelig kan den initieres med en vilkårlig verdi som er oppgitt av bruker
minimum_value = user_input_list[0]

#Nested for loop som først henter ut tallet som skal bli evaluert. Så evaluerer den om det tallet er mindre enn alle andre i listen
#Evaluerer også om tallet er mindre enn hva som for øyeblikket er det laveste tallet
#Kravet for at tallet for evaluering er dermed: må både være mindre enn tallet det blir sammenlignet med OG hva som foreløpig er det minste tallet som er evaluert
for number_for_evaluation in user_input_list:
    for number in user_input_list:
        if((number_for_evaluation < number) & (number_for_evaluation < minimum_value)):
            minimum_value = number_for_evaluation


print("minste verdi av dine tall er: ", minimum_value)

#Identisk kode og prinsipp som for minimum, men her er kravet at number_for_evlauation må være størren enn både nummeret og maximum_value
maximum_value = user_input_list[0]
for number_for_evaluation in user_input_list:
    for number in user_input_list:
        if((number_for_evaluation > number) & (number_for_evaluation > maximum_value)):
            maximum_value = number_for_evaluation


print("største verdi av dine tall er: ", maximum_value)
