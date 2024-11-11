def ultima_palavra(frase:str):
    
    listas_frases = frase.split(" ")
    ultimo_indice = len(listas_frases) - 1

    return listas_frases[ultimo_indice]