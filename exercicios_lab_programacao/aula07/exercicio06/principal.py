# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a
# uma grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e
# informe ao final o resultado da mesma. O programa deverá ler os valores até ser
# informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores
# além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções
# devem ser armazenados em uma lista. Após os dados terem sido completamente
# informados, o programa deverá calcular a percentual de cada um dos concorrentes e
# informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o
# seguinte:
# Sistema Operacional Votos %
# --------------------------- ------- ---
# Windows Server 1500 17%
# Unix 3500 40%
# Linux 3000 34%
# Netware 500 5%
# Mac OS 150 2%
# Outro 150 2%
# --------------------------- -----
# Total 8800
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40%
# dos votos.

import modulos 

os = ['Windows', 'Server' ,'Unix','Linux', 'Netware', 'Mac', 'Outro']
votes = []
while True:

    vote = input('[1]- Windows Server\n[2]- Unix\n[3]- Linux\n[4]- Netware\n[5]- Mac OS \n[6]- Other\n-> ')
    
    if vote == '0':
        break
    
    votes.append(vote)

sum_votes = modulos.count_votes(votes)
percen_sum_votes = modulos.percentage(votes, sum_votes)

print()

for i in range(len(os) - 1):
    print(f'{os[i]} - {sum_votes[i]} - %{percen_sum_votes[i]:.2f}')