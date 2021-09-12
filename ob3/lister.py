"""
Dette programmet:
- Starter en liste med integers og printer ut første og tredje entry i denne
- Oppretter en tom liste, for deretter å be bruker fylle den med fire navn
- Gir beskjed til bruker om hvorvidt et spesifisert navn er inkludert i listen
- Summerer og tar produktet av listen med integers, legger disse til første liste med integers for deretter å fjerne disse igjen
"""
list_integers = [1, 2, 3]

list_integers.append(4)

print(list_integers[0])
print(list_integers[2])

#Tom liste som skal fylles med navn gitt av bruker
list_names = []
#Definer lengde på listen og antall navn bruker skal oppgi
length_of_list = 4


for i in range(length_of_list):

    #Variabel for å beskrive hvor mange entires som gjenstår for bruker
    iter_list = length_of_list - i 
    list_names.append(input(f"Legg til totalt 4 navn i listen. {iter_list} av {length_of_list} gjenstår: "))

#Konverter list entires til små bokstaver for bedre treff på navn conditional
liste_input_lower = [item.lower() for item in list_names]

my_name = "marius"
is_name_in_list = my_name in liste_input_lower

if(is_name_in_list):
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#Starter sum og prod variabler
#tot_sum  må starte p¨å 0
#Tot prod må starte p å1 for ikke å endte på 0
tot_sum = 0
tot_prod = 1

for item in list_integers:
    tot_sum = tot_sum + item
    tot_prod = tot_prod * item
sum_and_prod = [tot_sum, tot_prod]

#Legg til sum og prod-liste i den gamle integerlisten 
list_extended = list_integers + sum_and_prod
print(list_extended)

#Fjern de to siste entries i den utvidede listen
entires_to_remove = 2
list_reduced = list_extended[:len(list_extended) - entires_to_remove]

print(list_reduced)
