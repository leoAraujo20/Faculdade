from func import *

menu = """
[1] Inserir usuário
[2] Listar nomes
[3] Listar dados de um usuário
[4] Listar dados do usuário de acordo com o ultimo acesso
[5] Alterar dados do usuário
[6] Excluir usuário
[7] Sair
Escolha: """
lista_usuarios = []

while True:
    escolha = input(menu)
    
    if escolha == '1':
       lista_usuarios.append(cadastro_usuario())

    elif escolha == '2':
        listar_nomes(lista_usuarios)

    elif escolha == '3':
        indice = int(input('Índice do usuário: '))
        listar_dados_usuario(lista_usuarios, indice)

    elif escolha == '4':
        data = input('Data: ')
        listar_data(lista_usuarios, data)
    
    elif escolha == '5':
        escolha_alteracao = input('[1] Alterar todos os dados\n [2] Nome\n [3] Acesso\n [4] Maquina\n escolha:')
        indice = int(input('Índice: '))
        alterar_dados(lista_usuarios, escolha, indice)

    elif escolha == '5':
        indice = int(input('Índice: '))
        deleta_usuario(lista_usuarios, indice)
    
    else:
        print('Fim do programa!')
        break

