def lucro(valor, quant):
    return valor * quant

def checa_lucro(custo, lucro):
    if custo < lucro:
        return("houve lucro!")
    elif custo > lucro:
        return("Houve prejuízo")
    else:
        return("A viagem se pagou!")

def tipo_mais_passageiros(passado,atual,tipo):
    if atual >= passado:
        return tipo
    return tipo

def mais_passageiros(passado,atual):
    if atual >= passado:
        return atual
    return passado