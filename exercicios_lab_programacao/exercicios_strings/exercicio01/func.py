def soma_cpf(cpf:str):
    lista1 = cpf.split('-')
    lista2 = lista1[0].split('.')
    lista2.append(lista1[1])
    
    soma = 0
    for valor in lista2:
       
        soma += int(valor)
    
    return soma


