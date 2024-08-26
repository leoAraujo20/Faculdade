import modulos

min_value = float(input('Min value for indemnity: '))
total_expenses = 0
biggest_b = 0
while True:
    footage = float(input('House footage(In M2): '))
    if footage == 0:
        break
    house_class = input("House class(A,B): ").upper()
    
    indemnity = modulos.indemnity(house_class,footage)
    if house_class == 'B':
        biggest_b = modulos.bigger(biggest_b,indemnity)

    print(f'Indemnity: ${indemnity}')

    total_expenses += indemnity

print(f'total expenses with compensation: ${total_expenses}')