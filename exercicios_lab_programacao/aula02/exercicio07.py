# Faça uma função que recebe por parâmetro o tempo representado em segundos e
# retorne esse tempo em horas, minutos e segundos. A hora completa deve ser retornada
# em uma variável no seguinte formato “Horas:Minutos:Segundos”, por exemplo, se for
# passado por parâmetro 3800 segundos para o método, este deverá retornar “1:3:20”,
# que indica, 1 hora, 3 minutos e 20 segundos. ATENÇÃO: Para formatar a variável de
# retorno, você precisará converter os valores para string. Para isso, utilize a função
# str(), que recebe um número inteiro por parâmetro e o converte para string.

def format_hours(total):
    hours = total // 3600
    minutes = (total % 3600) // 60
    seconds = (total % 3600) % 60
    return f"Hours:Minutes:Seconds \n {hours}:{minutes}:{seconds}"

total_seconds = int(input("How many seconds? "))
print(format_hours(total_seconds))