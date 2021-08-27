'''
Dette programmet:
- Slår sammen to navn gitt av bruker
- Beregner differanse av to statiske heltall
'''
navn = input("Vennligst oppgi navn:")
print("hei " + navn)

first_integer = 1
second_integer = 2

print(first_integer)
print(second_integer)

difference = first_integer - second_integer

#Konverter integer til string for å kunne concatenate
print("Differanse:" + str(difference))

nytt_navn = input("Vennligst oppgi nytt navn:")

sammen = f'{navn} og {nytt_navn}'
print(sammen)
