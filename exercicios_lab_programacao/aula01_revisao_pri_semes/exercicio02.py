# Escreva um programa que solicite um número ao usuário e determine se o número é
# par ou ímpar. Em seguida, imprima na tela uma mensagem indicando o resultado.

numero = int(input("Escolher numero:"))

resultado = "Par"
if numero % 2 != 0:
    resultado = "ímpar"

print(f"O numero escolhido é {resultado}")