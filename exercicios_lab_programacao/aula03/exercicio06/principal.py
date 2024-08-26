import modulos

eagle = modulos.eagle
dove = modulos.dove
human = modulos.human
cow = modulos.cow
flea = modulos.flea
caterpillar = modulos.caterpillar
leech = modulos.leech
worm = modulos.worm

while True:

    first_choice = input("Choose: vertebrate or invertebrate? ").lower()
    second_choice = input("Choose: bird, mammal, insect, or annelid? ").lower()
    third_choice = input("Choose: carnivore, omnivore, herbivore, or hematophagous? ").lower()

    choices = [first_choice, second_choice, third_choice]

    print('--------------------')
    modulos.print_list(choices)
    
    if choices == eagle:
        print('Your animal is:')
        print('Eagle!')
    
    elif choices == dove:
        print('Your animal is:')
        print('Dove')
    
    elif choices == human:
        print('Your animal is:')
        print('Human')
    
    elif choices == cow:
        print('Your animal is:')
        print('Cow')
    
    elif choices == flea:
        print('Your animal is:')
        print('Flea')

    elif choices == caterpillar:
        print('Your animal is:')
        print('Caterpillar')
    
    elif choices == leech:
        print('Your animal is:')
        print('Leech')
    
    elif choices == worm:
        print('Your animal is:')
        print('Worm')
    
    else:
        print('Your animal is:')
        print('Invalid!')