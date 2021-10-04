
"""
1.)
"""
def lagBrukernavn(navn, ordbok):

    
    navn_lower = navn.lower()

    #Split in two steps in case of names with middle names etc
    navn_split = navn_lower.split(" ")

    #Just extract the first two names in case user has several names
    first_name, last_name = navn_split[0:2]

    #Add only first letter from last name to user_name using [0]
    user_name = f'{first_name}{last_name[0]}'

    """
    6. bonus)
    """
    #Check if the username already exist. If it does, add one more letter
    user_name_exists = user_name in ordbok.keys()

    #Iterator for how many letters should be extracted form last name.
    #Defaults to two letter as the while loop is conditional on the username with only the first letter exists
    final_character = 2

    while user_name_exists:
        user_name = f'{first_name}{last_name[0:final_character]}'

        #Add numbers of characters from the last name until the user_name_exists == False
        final_character += 1

        user_name_exists = user_name in ordbok.keys()

        #TODO: when all characters from last name is exhausted, should use new rule to generate more

    return(user_name)




"""
2.)
"""

def lagEpost(brukernavn, suffix):

    return(f'{brukernavn}@{suffix}')



"""
3.)
"""

def skrivUtEposter(brukernavn_ordbok):


    for brukernavn in brukernavn_ordbok.keys():
        print(lagEpost(brukernavn, brukernavn_ordbok[brukernavn]))


"""
4.)
"""

def register_username():
    tom_ordbok = {}
    user_input = "default"

    while user_input != "s":

        user_input = input("Velg 'i' for å skrive inn navn og suffix. 'p' for å skrive ut epostene i ordboken. Velg 's' for å avslutte: ")

        if user_input == "i":
            
            name_input, suffix_input_raw = input("Skriv inn navn og epost-suffix. Separer dem med komma (,): ").split(",")
            #Fjerner eventuelt whitespace foran suffix
            suffix_input = suffix_input_raw.strip()

            username_input = lagBrukernavn(name_input, tom_ordbok)

            tom_ordbok[username_input] = suffix_input
        
        if user_input == "p":
            skrivUtEposter(tom_ordbok)

register_username()


"""
5.)
"""


def test_lagEpost():
    result_lagEpost = lagEpost("mariusl", "uio.no")
    correct_lagEpost = "mariusl@uio.no"
    assert result_lagEpost == correct_lagEpost, "Expected: " + correct_lagEpost + ", got: " + result_lagEpost
def test_skrivUtEposter():
    testordbok = {"olan": "ifi.uio.no", "karin":"student.matnat.uio.no"}
    result_skrivUtEposter = skrivUtEposter(testordbok)
    correct_skrivUtEposter = None
    assert result_skrivUtEposter == correct_skrivUtEposter
test_lagEpost()
test_skrivUtEposter()