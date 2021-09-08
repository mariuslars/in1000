'''
Dette programmet:
- Ber bruker oppgi antall grader i Fahrenheit og konverterer til Celcius
'''

#Gjør om input til int slik at math functions er mulig lenger ned
fahrenheit = int(input("Oppgi grader i Fahrenheit: "))

print(f'Temperatur i F: {fahrenheit}')

celsius = (fahrenheit - 32) * 5/9

print(f'Temperatur i C: {celsius}')

