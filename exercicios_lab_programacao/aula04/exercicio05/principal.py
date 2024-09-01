# Faça uma função que receba como parâmetro uma lista com 10 valores reais
# informados pelo usuário. A função deverá colocar todos estes valores em duas listas:
# uma somente de números pares e uma somente com os números ímpares. Estas listas
# deverão ser impressas pela função.

import modulos

numbers = []
for i in range(10):
    number = int(input('Type one number: '))
    numbers.append(number)

print(modulos.odd_even(numbers))