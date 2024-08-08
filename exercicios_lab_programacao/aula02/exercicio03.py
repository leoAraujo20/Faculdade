# Faça uma função que recebe um valor inteiro e retorna uma mensagem que informa se
# o valor é par ou ímpar.

def impar_par(n):
    n_checado = n % 2 == 0 
    if n_checado:
        return f"O número {n} é par."
    else:
        return f"O número {n} é impar."

numero = int(input("Escolha um numero:"))
print(impar_par(numero))