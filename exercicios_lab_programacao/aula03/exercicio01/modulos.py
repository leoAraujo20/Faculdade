def lucro(valor, quant):
    return valor * quant

def checa_lucro(custo, ganho):
    if custo < ganho:
        return("houve lucro!")
    elif custo > ganho:
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