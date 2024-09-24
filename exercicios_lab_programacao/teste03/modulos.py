def print_list(lista:list):
    lista_ordenada = lista.copy()
    lista_ordenada.sort()
    for value in lista_ordenada:
        print(value)

def adiciona_livro(lista, livro):
    lista.append(livro)

def remove_livro(lista, posicao):
    lista.pop(posicao - 1)
        
   

def modifica_livro(lista, posicao, nome):
        lista[posicao - 1] = nome
        
def verifiva_livro(lista, posicao):
    if posicao > len(lista) or posicao < 1:
        return False
    return True
            