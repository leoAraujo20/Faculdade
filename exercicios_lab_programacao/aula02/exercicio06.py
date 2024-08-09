# Faça uma função que recebe 3 valores inteiros por parâmetro e retorna-os ordenados
# em ordem crescente. Os valores retornados devem estar separados por vírgula (,) e para
# serem retornados como uma string, cada valor deve ser convertido para uma string com
# o uso da função str(), que recebe por parâmetro um número e retorna uma string.

def sorted(a, b ,c):
    if a >= b and a >= c:
        largest = a
        if b >= c:
            medium = b
            smaller = c
        else:
            medium = c
            smaller =  b
    
    elif b >= a and b >= c:
        largest = b
        if a >= c:
            medium = a
            smaller = c
        else:
            medium = c
            smaller = a

    else:
        largest = c
        if a >= b:
            medium = a
            smaller = b
        else:
            medium = b
            smaller = a
    
    return f"{str(smaller)}, {str(medium)}, {str(largest)}"

number1 = int(input("Type number 1:"))
number2 = int(input("Type number 2:"))
number3 = int(input("Type number 3:"))

print(sorted(number1,number2,number3))