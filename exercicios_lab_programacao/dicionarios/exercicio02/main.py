from func import *

objetos = [
    "Mesa", "cadeira", "LIVRO", "Caneta", "Lápis", "computador", 
    "Garrafa", "mesa", "TECLADO", "copo", "caneta", "LIVRO", 
    "Janela", "quadro", "Porta", "Relógio", "celular", "MOUSE",
    "televisão", "FONE", "lâmpada", "sofá", "LIVRO", "caderno", 
    "bolsa", "mochila", "agenda", "Caneta", "guarda-chuva", 
    "tapete", "Papel", "tijolo", "carteira", "Celular", "Fone", 
    "Chave", "colher", "faca", "mesa", "cadeira"
]

objetos_minusculo = []
for objeto in objetos:
    objetos_minusculo.append(objeto.lower())

dicionario_quantidades = cont(objetos_minusculo)

soma_total = total(dicionario_quantidades)

for chave, valor in dicionario_quantidades.items():
    print(f'{chave}: {valor}')
print('Total:', soma_total)


