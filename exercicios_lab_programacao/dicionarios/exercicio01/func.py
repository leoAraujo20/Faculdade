def cadastro_usuario():
    dados_usuario = {}
    dados_usuario['login'] = input('Login: ')
    dados_usuario['nome'] = input('Nome: ')
    dados_usuario['acesso'] = input('Ultimo acesso: ')
    dados_usuario['maquina'] = input('Maquina: ')
    return dados_usuario

def listar_nomes(lista_usuarios:list[dict]):
    for usuario in lista_usuarios:
            print(f'Nome: {usuario['nome']}')

def listar_dados_usuario(lista_usuarios: list[dict], indice_usuário):
     for chave, valor in lista_usuarios[indice_usuário].items:
          print(f'{chave}: {valor}')

def listar_data(lista_usuarios, data):
     for usuario in lista_usuarios:
          if usuario['acesso'] == data:
               for chave, valor in usuario.items:
                    print(f'{chave}: {valor}')

def alterar_dados(lista_usuarios, escolha, indice):
    if escolha == '1':
        nome = input('Nome: ')
        acesso = input('Acesso: ')
        maquina = input('Maquina: ')

        lista_usuarios[indice].update({'nome': nome, 'acesso': acesso, 'maquina': maquina})
    
    elif escolha == '2':
         lista_usuarios[indice].update({'nome': nome})

    elif escolha =='3':
         lista_usuarios[indice].update({'acesso': acesso})
        
    elif escolha =='4':
         lista_usuarios[indice].update({'maquina': maquina})

def deleta_usuario(lista_usuarios, indice):
     del lista_usuarios[indice]

