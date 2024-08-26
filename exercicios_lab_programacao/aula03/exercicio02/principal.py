import modulos

bill = 0
while True:
    
    menu = modulos.cardapio
    modulos.menu(menu)
    usar_order = int(input('Chose your item: '))
    order_quantity = int(input('How many? '))

    order_checked = modulos.valid_choice(usar_order,menu)
    order_price = modulos.realize_order(order_quantity,menu[order_checked][1])
    print('----Your order----')
    print(f'{menu[order_checked][0]} - {order_quantity}: ${order_price}')
    bill += order_price
    
    again = input("Make another order?[Y]es [N]o: ").upper()
    if again == 'N':
        break

print(f'Final check: ${bill}')