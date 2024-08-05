quant = int(input("Quantos numeros serão digitados:"))

cont = 0
soma = 0
while cont < quant:
    numero = int(input("Digitar valor:"))
    soma = soma + numero
    cont += 1

media = soma / quant

print(f"A média dos valores é: {media}")