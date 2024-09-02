# Faça uma função que receba uma lista como parâmetro e retorne True caso haja
# algum elemento que apareça mais de uma vez e False caso contrário. Ela não deve
# modificar a lista original.

import modulos

list_with_duplicates = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
list_without_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(modulos.has_duplicates(list_with_duplicates))
