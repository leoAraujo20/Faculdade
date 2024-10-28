def primeiras_palavras(frase:str):
    
    lista_frase = frase.split(" ")
    penultimo_indice = len(lista_frase) - 2 

    lista_primeiras = lista_frase[:penultimo_indice]
    return lista_primeiras