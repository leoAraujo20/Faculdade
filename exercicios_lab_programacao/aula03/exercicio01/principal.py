import modulos

maior = 0
quant_viagem_a = 0
while True:
    tipo_viagem = input("Tipo da viagem(A, B, C): ").upper()
    
    if tipo_viagem == "X":
        break

    data = input("Data da viagem: ")
    quant_passageiros = int(input("Quantidade de passageiros: "))
    valor_passagem = float(input("Valor da passagem: "))
    despesas = float(input("Despesas: "))
    lucro = modulos.lucro(valor_passagem, quant_passageiros)

    print()
    print(f"Viagem do dia {data}:")
    print(modulos.checa_lucro(despesas, lucro))

    if tipo_viagem == "A":
        quant_viagem_a += 1
    
    elif tipo_viagem == "B":
        if data == "23/12/22":
            quantidade_data_especifica = quant_passageiros

    tipo_mais_passageiros = modulos.tipo_mais_passageiros(maior, quant_passageiros,tipo_viagem)
    maior = modulos.mais_passageiros(maior,quant_passageiros)

print(f"Quantidade de viagens do ônibus 'A':{quant_viagem_a}")
print(f"Ônibus com mais passageiros {maior}")
print(f"Quantidades de passageiros que viajaram no ônibus B em 23/12/22: {quantidade_data_especifica}")
