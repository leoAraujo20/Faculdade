# Considere uma lista composta por listas de números reais. Faça uma função que
# receba uma lista deste tipo e calcule a média dos valores de cada lista interna,
# inserindo-os ao fim de cada uma delas. No fim da lista externa deve ser inserida a
# média geral dos valores de todas as listas. A função deverá retornar esta lista.

import modulos

list_of_floats = [
    [1.5, 2.8, 3.1, 4.6],
    [5.0, 6.2, 7.3],
    [8.9, 9.1, 10.5, 11.7],
    [12.3, 13.6],
    [14.8, 15.2, 16.9]
]

print(modulos.average(list_of_floats))

