def primeiras_palavras(frase:str):
    
    lista_frase = frase.split(" ")
    ultimo_indice = len(lista_frase) - 1

    lista_primeiras = lista_frase[:ultimo_indice]
    return lista_primeiras