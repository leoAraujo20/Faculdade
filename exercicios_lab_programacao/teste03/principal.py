import modulos 

livros = []
while True:
    escolha = input('[1]Registrar livros\n[2]Listar livros\n[3]Excluir livro\n[4]Alterar livro\n[5]Sair\n-> ')
    
    if escolha == '1':
        print()
        livro = input('Digitar nome do livro: ')
        modulos.adiciona_livro(livros, livro)
        print('Livro adicionado!')
        print()
    
    elif escolha == '2':
        print()
        print('LIVROS:')
        modulos.print_list(livros)
        print()
        
    
    elif escolha == '3':
        print()
        posicao_livro = int(input('Digitar posiçõão do livro para excluir: '))
        
        if not modulos.verifiva_livro(livros, posicao_livro):
            print()
            print('Ocorreu um erro!')
            print()
            continue
        
        modulos.remove_livro(livros, posicao_livro)
        print('Livro removido com sucesso!')
    
    elif escolha == '4':
        
        print()
        posicao_modificar = int(input('Digitar posiçõão do livro para modificar: '))
        novo_nome = input("Digite o novo nome para o livro: ")
        
        if not modulos.verifiva_livro(livros, posicao_modificar):
            print()
            print('Ocorreu um erro!')
            print()
            continue

        modulos.modifica_livro(livros, posicao_modificar, novo_nome)
        print('Livro modificado com sucesso!')
        print()    
    
    elif escolha == '5':
        break

    else:
        print()
        print('Escolha inválida')
        print()

        

   