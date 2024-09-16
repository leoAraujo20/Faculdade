# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
# vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por
# cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve
# vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou
# seja, um total de $470. Escreva um programa que determine quantos vendedores
# receberam salários nos seguintes intervalos de valores:
# a. $200 - $299
# b. $300 - $399
# c. $400 - $499
# d. $500 - $599
# e. $600 - $699
# f. $700 - $799
# g. $800 - $899
# h. $900 - $999
# i. $1000 em diante

import modulos

amount = []
while True:
    week_amount = float(input('Amount raised during the week:'))
    if week_amount == 0:
        break
    amount.append(modulos.wage(week_amount))

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

for value in amount:
    
    if value >= 200 < 300:
        a += 1
    elif value >= 300 < 400:
        b += 1
    elif value >= 400 < 500:
        c += 1
    elif value >= 500 < 600:
        d += 1
    elif value >= 600 < 700:
        e += 1
    elif value >= 700 < 800:
        f += 1
    elif value >= 800 < 900:
        g += 1
    elif value >= 900 < 1000:
        h += 1
    else:
        i += 1

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)



