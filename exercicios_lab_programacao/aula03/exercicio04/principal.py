import modulos

while True:
    print('\n[1]Can vote? \n[2]Age category: \n[3]Can enlist? \n[4]End execution: ')
    user_input = input('Chose one action:')
    
    if user_input == '1':
        age = int(input('Enter your age: '))
        print(modulos.can_vote(age))

    elif user_input == '2':
        age = int(input('Enter your age: '))
        print(modulos.age_category(age))
    
    elif user_input == '3':
        age = int(input('Enter your age: '))
        gender = input('Enter your gender [M]ale [F]emale: ')
        print(modulos.enlistment_age(age, gender))
    
    else:
        print('\nProgram ended!')
        break