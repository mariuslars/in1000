"""
Dette programmet:
- Definerer to hjelpefunksjoner. én for å finne hvor mange bokstaver i et ord. Én for å lage en ordbok over unike ord og antall forekomster i en setning
- Definerer en funksjon som analyserer antall unike ord, forekomster av disse og lengden på disse ordene og skriver resultatet tilbake til bruker
"""



#1.)
def finn_antall_bokstaver(ord):
    #Finner og returnerer antall bokstaver i et ord
    return(len(ord))

#2.)
def generer_ordbok(setning):
    """ 
    Returnerer en ordbok hvor ordet i setningen er key og antall forekomster av dette er value
    Input er en setning som string
    """
    setning_liste = setning.split(" ")

    #Konverterer listen til mengde for å kun beholde unike ord. 
    setning_mengde = set(setning_liste)
    
    #Setter opp dictionary for å legge til verdier senere
    setning_ordbok = dict.fromkeys(setning_mengde)

    #Start teller som benyttes for å telle antall forekomster per ord
    word_counter = 0

    #Nested for loop hvor vi først henter ut ett og ett ord fra mengden og evaluerer dette mot alle ord i listen.
    #For hvert treff legger vi til 1 i word_counter
    for word_for_evaluation in setning_mengde:
        for word in setning_liste:
            if(word_for_evaluation == word):
                word_counter += 1
        
        setning_ordbok[word_for_evaluation] = word_counter

        #Restarter word_counter for hvert ord i mengden
        word_counter = 0
    

    return(setning_ordbok)


#3.)

def analyse_user_sentence():

    sentence = input("Skriv inn en setning: ")

    #Do analysis of sentence and print results
    sentence_list = sentence.split()
    sentence_length = len(sentence_list)
    sentence_set = set(sentence_list)

    print(f"Det er {sentence_length} ord i setningen din")

    #Do analysis of words in sentence and print results
    dictionary_sentence = generer_ordbok(sentence)

    #Iterate over all unique words in the sentence 
    for word in sentence_set:

        #Get the value from the dictionary
        number_occurrence = dictionary_sentence[word]
        word_length = finn_antall_bokstaver(word)
        
        #Adjust output word to account for single letter words and single occurrences
        dynamic_bokstav_string = "bokstaver"
        if(word_length == 1):
            dynamic_bokstav_string = "bokstav"

        dynamic_gang_string = "ganger"
        if(number_occurrence == 1):
            dynamic_gang_string = "gang"

        print(f'Ordet "{word}" forekommer {number_occurrence} {dynamic_gang_string}, og har {word_length} {dynamic_bokstav_string}')
        
    
    



analyse_user_sentence()
