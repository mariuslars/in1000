'''
Oppgave:
- Skriv et quiz-program som består av 3 spørsmål. 
- Hvert spørsmål gir 1 poeng for riktig, 0 for galt
- Skriv ut total poengsum etter alle tre spørsmål er besvart
'''

def question(question_string, correct_answer):
    
    #Print spørsmål og be om svar fra quiz-deltaker
    answer = input(question_string)

    if(answer == correct_answer):
        poeng = 1
        print("Riktig svar.")
    else:
        print("Galt svar.")
        poeng = 0
    
    return(poeng)

def ask_questions():

    #Nye spørsmål og svar legges til i følgende lister
    question_list = ["Hva er hovedstaden i Norge? ", "Hvordan forkortes 'personal computer'? ", "Hvor mange fylker har Norge per 1. januar 2020? "]
    answer_list = ["Oslo", "PC", "11"]

    #Legger antall spørsmål til i et objekt for gjenbruk senere
    number_of_questions = len(question_list)

    #Start poengteller. Hvis answer == correct_answer legges 1 poeng til for hvert riktige svar.
    antall_poeng = 0
    for i in range(number_of_questions):
        antall_poeng = antall_poeng + question(question_list[i], answer_list[i])

    print(f'Du fikk {antall_poeng} poeng av {number_of_questions} mulige')

ask_questions()