# Faça uma função que recebe as 3 notas de um aluno por parâmetro e uma letra, que
# indicará o tipo da média a ser calculada. Caso a letra seja A, a função deve calcular a
# média aritmética das notas do aluno, se for P, deve ser calculada a média ponderada
# (pesos: 5, 3 e 2 respectivamente). O cálculo da média deve ser retornado pela função.
# Na chamada da função, as 3 notas devem ser informadas pelo usuário e as notas podem
# ser fracionadas (por exemplo, 7.5 ou 8.5).

def test_average(t1,t2, t3,grade_average_type):
    if grade_average_type == "a":
        average = (t1 + t2 + t3)/3
    else:
        average = (t1 * 5 + t2 * 3 + t3 *2) / 9 
    return average

test1 = float(input("Test 1: "))
test2 = float(input("Test 2: "))
test3 = float(input("Test 3: "))
grade_type = input("Average type: ").lower()

print(test_average(test1,test2,test3,grade_type))