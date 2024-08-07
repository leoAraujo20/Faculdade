# Faça um programa que solicite ao usuário o valor de um produto e aplique um
# desconto de 10%. Em seguida, exiba o valor final com o desconto aplicado.

valor = float(input("Valor: "))

valor_desconto = valor - (valor * 0.1)

print(f"O valor com desconto é R$:{valor_desconto:.2f}")