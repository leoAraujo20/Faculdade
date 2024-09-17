def print_list(lista:list):
    lista_ordenada = lista.copy()
    lista_ordenada.sort()
    for value in lista_ordenada:
        print(value)

def adiciona_livro(lista, livro):
    lista.append(livro)

def remove_livro(lista, posicao):
    try:
        lista.pop(posicao)
        return True
    except:
        return False

def modifica_livro(lista, posicao, nome):

    try:
        lista[posicao] = nome
        return True
    except:
        return False
    
            