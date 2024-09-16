# Crie um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
# Ao final, o programa emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
# contrário, ele será classificado como "Inocente"

from modulos import classify

question1 = (input('Telefonou para a vítima?[S]im [N]ão: '))
question2 = (input('Esteve no local do crime?[S]im [N]ão: '))
question3 = (input('Mora perto da vítima?[S]im [N]ão: '))
question4 = (input('Devia para a vítima?[S]im [N]ão: '))
question5 = (input('Já trabalhou com a vítima?[S]im [N]ão: '))

answers = [question1, question2, question3, question4, question5]

print(classify(answers))