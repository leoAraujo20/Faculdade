from modulos import verifica_situacao

alunos = []
notas = []
aprovados = 0
reprovados = 0

while True:

    nome_aluno = input("Digitar mome de aluno: ")
    alunos .append(nome_aluno)
    
    if nome_aluno == 'SAIR':
        break
    
    notas_aluno = []
    nota1 = float(input("Digitar nota do primeiro bimestre:"))
    notas_aluno.append(nota1)
    nota2 = float(input("Digitar nota do segundo bimestre:"))
    notas_aluno.append(nota2)
    nota3 = float(input("Digitar nota do terceiro bimestre:"))
    notas_aluno.append(nota3)
    nota4 = float(input("Digitar nota do quarto bimestre:"))
    notas_aluno.append(nota4)
   

    notas.append(notas_aluno)

situacoes = []
for i in range(len(alunos) - 1):
    situacoes.append(verifica_situacao(notas[i][0], notas[i][1], notas[i][2], notas[i][3]))

for status in situacoes:
    if status == 'APROVADO!':
        aprovados += 1
    else:
        reprovados += 1

print()
print('Escola Privamera - Gestão de Alunos')
print('----------------------------')
for i in range(len(alunos) - 1):
    print(f'{alunos[i]} - {situacoes[i]}')

print()
print('Total alunos:')
print(f'Aprovados = {aprovados}')
print(f'Reprovados = {reprovados}')