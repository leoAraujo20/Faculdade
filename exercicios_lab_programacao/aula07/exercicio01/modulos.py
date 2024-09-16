def classify(answers_list:list):
    
    cont = answers_list.count('S')
    
    if cont < 2:
        return 'INNOCENT!'
    elif cont == 2:
        return 'SUSPECT!'
    elif cont <= 4:
        return 'ACCOMPLICE!'
    else:
        return 'ASSASSIN!' 
