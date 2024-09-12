def verifica_situacao(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
        return 'APROVADO!'
    return 'REPROVADO!'