def cont(lista):
    cont_objetos = {}
    for objeto in lista:
        if objeto not in cont_objetos:
            cont_objetos[objeto] = lista.count(objeto)
    return cont_objetos

def total(dicionario: dict):
    total = 0
    for value in dicionario.values():
        total += value 
    
    return total