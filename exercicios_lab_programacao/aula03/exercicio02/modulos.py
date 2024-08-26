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
    if user_order < len(menu) and user_order >= 0:
        return user_order
    else:
        return

def realize_order(quant,price):
    order_price = price * quant
    return order_price
    