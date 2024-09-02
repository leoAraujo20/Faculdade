# Crie uma função que receba como parâmetro um valor inteiro e retorne uma lista de
# inteiros preenchida de forma aleatória de acordo com a quantidade especificada no
# parâmetro.
# Dica: para gerar valores aleatórios pesquise pelo módulo random do Python no
# Google.
# Ex.:
# Parâmetro: 5
# Lista retornada = [3, 2, 5, 4, 1]

import modulos

range_list = int(input('how many numbers?' ))

print(modulos.create_random_list(range_list))