def checa_parentesco(frase:str, lista:list):
    lista_palavras = frase.split(" ")

    ultimo_indice = len(lista_palavras) - 1 
    if lista_palavras[ultimo_indice] in lista:
        return True
    
    return False

