def somaValores(lista):
    return sum(lista)

def menorValor(lista:list):
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = lista[0]
        return menor

def quantidade(lista: list, valor):
    quant_valor = lista.count(valor)
    return quant_valor

def quantidadeVarios(lista:list, *args):
    quantidade_valores = []
    for valor_checar in args:
        valor_checado = lista.count(valor_checar)
        quantidade_valores.append(valor_checado)
    
    for valor in quantidade_valores:
        print(valor)

def imprimeUltimosXValores(lista:list,começo):
    ultimosXValores = lista[-começo:]
    ultimosXValores.reverse()
    for valores in ultimosXValores:
        print(valores)

def somaIntervalo(lista:list, começo, fim):
    soma = 0
    for x in range(começo,fim+1):
        soma += lista[x]
    return soma

def imprimeParesOrdemCrescente(lista):
    lista_pares_ordem_crescente = []
    for valor in lista:
        if valor % 2 == 0:
            lista_pares_ordem_crescente.append(valor)
    lista_pares_ordem_crescente.sort()

    for valor in lista_pares_ordem_crescente:
        print(valor) 

def imprimeImparesOrdemDecrescente(lista):
    lista_impares_ordem_crescente = []
    for valor in lista:
        if valor % 2 != 0:
            lista_impares_ordem_crescente.append(valor)
    lista_impares_ordem_crescente.sort()
    lista_impares_ordem_crescente.reverse()

    for valor in lista_impares_ordem_crescente:
        print(valor) 

def imprimeVizinhosADireitaDeX(lista, valor):
    for x in range(len(lista) - 1):
        if lista[x] == valor:
            print(lista[x + 1])