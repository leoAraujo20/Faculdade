# Faça uma função que verifique se um valor é perfeito ou não. Um valor é perfeito
# quando ele é igual a soma dos seus divisores, exceto ele próprio. (por exemplo, 6 é
# perfeito, pois 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor
# booleano: True se é perfeito e False se não for perfeito. Pesquise na internet por outros
# números considerados perfeitos e teste sua função.

def perfect_value(number):
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            sum += i
    is_perfect = number == sum
    return f"Is the number perfect ? {is_perfect}"

print(perfect_value(6))


