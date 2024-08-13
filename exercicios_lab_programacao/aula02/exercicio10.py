# Faça uma função que recebe 3 valores reais X, Y e Z e que verifica se esses valores podem
# ser os comprimentos dos lados de um triângulo. Caso seja um triângulo, deve retornar
# o tipo que triângulo que os lados formam, caso contrário retorna uma mensagem
# informando que não é um triângulo.
# Obs: Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade
# seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do
# comprimento dos outros dois lados.
# A função deve identificar o tipo de triângulo formado observando as seguintes
# definições:
# Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
# Triângulo Isósceles: os comprimentos de 2 lados são iguais.
# Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.

def type_triangle(x, y ,z):
    if x < y + z and y < x + z and z < x + y:
        if x == y and y == z:
            return "Equilateral"
        elif x == y or x == z or y == z:
            return "Isosceles"
        else:
            return "Escalene"
    
    else:
        return "It's not a triangle"

side1 = float(input("First side: "))
side2 = float(input("Second side: "))
side3 = float(input("Third side: "))

print(type_triangle(side1, side2 , side3))