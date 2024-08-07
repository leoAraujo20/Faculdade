# Crie um jogo de adivinhação de números da seguinte forma:
# O computador deve selecionar aleatoriamente um número inteiro entre 0 e 100.
# * Pesquise como pegar valores aleatórios (randômicos no Python).
# O computador fica solicitando números ao jogador, até que ele adivinhe o número
# selecionado, sendo que a cada tentativa errada do usuário, o computador deve
# informar se o palpite digitado é maior ou menor que o número selecionado (que
# deve ser encontrado).
# Quando o jogador acertar o número, deve ser apresentada uma mensagem com o
# seguinte modelo:
# ****************************************
# Parabéns!!!! O número correto é 41
# Quantidade de tentativas --> 9
# ***************************************
# Após a finalização da partida, o computador faz a pergunta “Jogar novamente?”,
# sendo que fica em execução enquanto o usuário responder ‘s’ para essa pergunta.

from random import randint

numero_computador = randint(0,100)
print("\nO jogo começõu, ja escolhi meu número! \n")
numero_pessoa = int(input("Qual numero eu escolhi? "))

tentativas = 0
while numero_computador != numero_pessoa:
    if numero_pessoa > numero_computador:
        print("O numero que vc escolheu é maior! \n")
    elif numero_pessoa < numero_computador:
        print("O numero que vc escolheu é menor! \n")
    tentativas += 1
    
    numero_pessoa = int(input("Escolha outro número:"))

print("****************************************")
print(f"Parabéns!!!! O número correto é {numero_computador}")
print(f"Quantidade de tentativas --> {tentativas}")
print("****************************************")