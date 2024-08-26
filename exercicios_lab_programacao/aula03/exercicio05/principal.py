import modulos

min_salary = float(input('Enter the minimum wage: '))
total_expenses = 0
least_sales = 10000000000000
least_sales_seller = None
while True:
    seller = input("Name of the seller ([L]eave): ").upper()
    if seller == 'L':
        break
    quant = int(input('number of t-shirts sold: '))

    seller_wage = modulos.payment(min_salary,quant)
    seller_category = modulos.category(seller_wage)
    
    if seller_wage <= least_sales:
        least_sales_seller = seller
        least_sales = seller_wage

    total_expenses += seller_wage
    print(f'\nSeller:{seller}\nValue to receive:${seller_wage:.2f}\nCategory:{seller_category}\n')

print()
print(f'Total expenses: ${total_expenses:.2f}')
print(f'seller who sold less: {least_sales_seller}')