# Considere uma lista composta por listas de números inteiros. Faça uma função que
# receba uma lista deste tipo e que imprima o maior número existente em cada uma das
# listas internas e o maior número no geral.

import modulos

list_of_integers = [
    [3, 5, 7, 9],
    [12, 14, 16],
    [21, 23, 25, 27, 29],
    [1, 4, 6, 8],
    [100, 200, 300]
]

print(modulos.biggest(list_of_integers))