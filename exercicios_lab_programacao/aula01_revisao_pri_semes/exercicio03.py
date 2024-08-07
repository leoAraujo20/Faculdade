# Desenvolva um programa que receba a idade do usuário e determine se ele é maior de
# idade (idade igual ou superior a 18 anos). Em seguida, exiba uma mensagem indicando
# se ele é maior de idade ou não.

idade = int(input("Qual a idade? "))

resultado = "Menor"
if idade >= 18:
    resultado =  "Menor"

print(f"A pessoa é {resultado} de idade!")