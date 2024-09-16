# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O
# resultado do atleta será determinado pela média dos cinco valores restantes. Você
# deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
# atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O
# programa deve ser encerrado quando não for informado o nome do atleta. A saída do
# programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

import modulos 

while True:
    jumps = []
    name = input('Athlete name: ')
    if not name:
        break
    jump1 = float(input('Jump 1: '))
    jumps.append(jump1)
    jump2 = float(input('Jump 2: '))
    jumps.append(jump2)
    jump3 = float(input('Jump 3: '))
    jumps.append(jump3)
    jump4 = float(input('Jump 4: '))
    jumps.append(jump4)
    jump5 = float(input('Jump 5: '))
    jumps.append(jump5)

    print('Final result:')
    print(f'Athlete: {name}')
    print(f'Jumps: {modulos.print_list(jumps)}')
    print(f'Average: {modulos.calculate_average(jumps)}')