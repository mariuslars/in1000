first_day, first_month = input("oppgi dato i format: dag måned, for eksempel 01 10 er 1. oktober: ").split()
#Gi respons til bruker
print(f'du har registrert: {first_day} {first_month}')

second_day, second_month = input("oppgi en ny dato i samme format som over: ").split()
print(f'du har registrert: {second_day} {second_month}')

first_day, first_month = int(first_day), int(first_month)
second_day, second_month = int(second_day), int(second_month)

#print(first_day)
#print(second_day)

if first_month < second_month:
    print("Riktig rekkefølge!")
elif first_month > second_month: 
    print("Feil rekkefølge!")
else:
    if first_day < second_day:
        print("Riktig rekkefølge")
    elif first_day > second_day:
        print("Feil rekkefølge")
    else:
        print("Samme dato!")

