'''
1) Programmet vil kun kjøre hvis b >= 10. Hvis b < 10 vil den forsøke å concatenate string og integer samme. Dette vil gi feilmelding
2) Så lenge b >= 10 vil det ikke oppstå noen problemer. Hvis b < 10 vil man få feilmelding
'''
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")