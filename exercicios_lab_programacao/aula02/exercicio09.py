# Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e
# retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula peso ideal
# = 72.7 x alt - 58 e ,para mulheres, peso ideal = 62.1 x alt - 44.7.

def idel_weight(height, gender):
    if gender == "M":
        weight = 72.7 * height - 58
    elif gender == "F":
        weight = 62.1 * height - 44.7
    return weight

person_weight = float(input("How tall are you?"))
person_gender = input("what is your gender")

print(idel_weight(person_weight, person_gender))