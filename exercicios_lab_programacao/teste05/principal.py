import modulos

salarios = []
colaboradores = []
gastos_totais = 0
abono_200 = 0

while True:
    nome_colaborador = input('Digitar nome do colaborador ("SAIR" para enecerrar): ')
    
    if nome_colaborador =='SAIR':
        break
    
    salario_colaborador = float(input('Digitar salario do colaborador: '))
    colaboradores.append(nome_colaborador)

    abono_colaborador = modulos.abono(salario_colaborador)
    if abono_colaborador == 200:
        abono_200 += 1
    
    salario_final = salario_colaborador + abono_colaborador
    
    salarios.append(salario_final)

    gastos_totais += salario_final

quant_colaboradores = len(colaboradores)
print()
print('PROJEÇÃO DE GASTOS COM ABONOS!')
print('===============================')
for i in range(len(colaboradores)):
    print(f'{colaboradores[i]} -> Total: R${salarios[i]}')
print('-------------------------------------')
print(f'Total(Salarios + abonos): R$:{gastos_totais}')
print(f'Foram processados {quant_colaboradores} colaboradores')
print(f'Valor mínimo pago a {abono_200} colaborador(es)')


    