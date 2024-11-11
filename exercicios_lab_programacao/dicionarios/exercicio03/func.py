def checa_palavra(dicionario:dict, palavra):
    if palavra in dicionario.keys():
        print(f'{palavra} = {dicionario[palavra]}')