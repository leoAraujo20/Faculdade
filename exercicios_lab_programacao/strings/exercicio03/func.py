def ultimas_palavras(frase:str):
    
    lista_frase = frase.split(" ")
    penultimo_indice = len(lista_frase) - 2 

    lista_ultimos = lista_frase[penultimo_indice:]
    return " ".join(lista_ultimos)