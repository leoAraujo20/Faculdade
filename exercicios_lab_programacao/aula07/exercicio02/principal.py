# Faça um programa que leia um número indeterminado de valores, correspondentes a
# notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que
# não deve ser armazenado). Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do
# outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo
# do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem;

import modulos

number_list = []
while True:
    number = int(input('Type one number: '))
    if number == -1:
        break
    number_list.append(number)

modulos.print_list(number_list)
print()
modulos.reverse_list(number_list)
print()
print(modulos.total_sum(number_list))
print()
print(modulos.calculate_average_grade(number_list))
print()
modulos.above_average(number_list, modulos.calculate_average_grade(number_list))
print()
modulos.above7(number_list)
print()
print('program terminated')
