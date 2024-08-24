cardapio = [['Cachorro-quente',5.00],
['X-Salada', 10.00],
['X-Bacon', 12.00],
['Bauru', 8.00],
['Refrigerante', 4.00],
['Suco', 6.00]]

def menu(cardapio):
    print('----Cardápio----')
    for produto, preco in cardapio:
        print(f'{produto}-{preco}')
    return

def valid_choice(user_order,menu):
    if 0 <= user_order < len(menu): 
        return user_order
    else:
        return

def realize_order(choice,menu):
    if not choice:
        return 'Choice is not valid'
    return choice