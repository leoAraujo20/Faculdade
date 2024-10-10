from provaG1 import *

lista= [12, 0, 34, 21, 34, 13, 65, 21, 12, 13, 34, 21, 12, 12, 65, 57, 12]

#somaValores: 0,5
print('A soma dos valores da lista é:', somaValores(lista))

#menorValor: 0,5
print('O menor valor da lista é:', menorValor(lista))

#quantidade: 0,5
print('Quantidade de 12 na lista é:', quantidade(lista, 12))

#quantidadeVarios: 0,5
print('As quantidades de 13, 65, 15 e 57 na lista são:')
quantidadeVarios(lista, 13, 65, 15, 57)

#imprimeUltimosXValores: 0,5
print('Os últimos 10 valores da lista são:')
imprimeUltimosXValores(lista, 10)
print('Os últimos 5 valores da lista são:')
imprimeUltimosXValores(lista, 5)

#somaIntervalo: 0,5
print('A soma dos valores do intervalo de 0 a 5 da lista é:', somaIntervalo(lista, 0, 5))
print('A soma dos valores do intervalo de 11 a 15 da lista é:', somaIntervalo(lista, 11, 15))

#imprimeParesOrdemCrescente: 0,5
print('A lista de valores pares em ordem crescente fica assim:')
imprimeParesOrdemCrescente(lista)

#imprimeImparesOrdemDecrescente: 0,5
print('A lista de valores ímpares em ordem decrescente fica assim:')
imprimeImparesOrdemDecrescente(lista)

# Bônus: +0,5
#imprimeVizinhosADireitaDeX
print('Cada valor 12 na lista tem como vizinhos à direita')
imprimeVizinhosADireitaDeX(lista, 12)
