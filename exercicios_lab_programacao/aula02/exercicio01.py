# Faça uma função que recebe por parâmetro um valor inteiro e retorne o valor lógico
# Verdadeiro (True) caso o valor seja positivo e Falso (False) caso contrário.

def positive_or_negative(valor):
    is_positive = valor >= 0
    return is_positive

user_choice = int(input("Chose your number: "))

print(F"Is the number positive? {positive_or_negative(user_choice)}")