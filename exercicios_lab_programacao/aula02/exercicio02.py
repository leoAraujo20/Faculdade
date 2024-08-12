# Crie uma função que que receba como parâmetro um valor lido do teclado e imprima para
# o usuário, a mensagem “O valor {N} informado é positivo” ou a mensagem “O valor {N}
# informado é negativo”.

def positive_or_negative(value):
    if value > 0:
        print(f"O valor {value} informado é positivo")
    elif value < 0:
        print(f" valor {value} informado é negativo")
    else:
        print(f"Valor {value} informado é nulo")

chosen_value = int(input("Chose your number to check: "))

positive_or_negative(chosen_value)