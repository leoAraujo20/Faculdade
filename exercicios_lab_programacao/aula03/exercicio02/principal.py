import modulos

while True:
    
    menu = modulos.cardapio
    modulos.menu(menu)
    usar_order = int(input('Chose your item: '))

    order = modulos.valid_choice(usar_order,menu)
    print(modulos.realize_order(order,menu))
    
    break