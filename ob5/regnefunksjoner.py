"""
Dette programmet:
"""

#1.)
def addisjon(x, y):

    return x + y

print(addisjon(1, 1336))

#2.)

def subtraksjon(x, y):

    return x - y

def divisjon(x, y):

    return x / y

def assert_addisjon():
    assert addisjon(3, 1) == 4
    assert addisjon(-3, -1) == -4
    assert addisjon(4, -1) == 3

def assert_subtraksjon():
    assert subtraksjon(3, 1) == 2
    assert subtraksjon(-3, -1) == -2
    assert subtraksjon(4, -1) == 5

def assert_divisjon():
    assert divisjon(3, 1) == 3
    assert divisjon(-3, -1) == 3
    assert divisjon(4, -1) == -4



assert_addisjon()
assert_subtraksjon()
assert_divisjon()

#3.)

def tommerTilCm(antallTommer):

    assert antallTommer > 0, "antallTommer må være større enn 0"

    return antallTommer * 2.54

print(tommerTilCm(1))

#4.)

def skrivBeregninger():

    input_1, input_2 = float(input("skriv in to tall, separert med ',' (komma) som skal adderes, subtraheres, og divideres: ").split(","))
    
    print(addisjon(input_1, input_2))
    print(subtraksjon(input_1, input_2))
    print(divisjon(input_1, input_2))

    input_tommer = float(input("skriv inn et tall som skal konverteres fra tommer til centimeter: "))

    print(tommerTilCm(input_tommer))

