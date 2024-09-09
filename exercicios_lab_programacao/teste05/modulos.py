def abono(salario):
    abono =  salario * 0.25
    if abono < 200:
        abono = 200
        return abono
    return abono

# def print_lista(lista):
#     for valor in lista:
#         print(valor)
