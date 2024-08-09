# Faça uma função que recebe a idade de uma pessoa em anos, meses e dias (um
# parâmetro para anos, outro para meses e outro para dias) e retorne essa idade em dias.
# Considere que um ano tem 360 dias e os meses são de 30 dias.

def days_lived(years, months, days):
    return years * 360 + months * 30 + days

years = int(input("How many years? "))
months = int(input("How many month? "))
days = int(input("How many days? "))

print(f"You have been alive for {days_lived(years, months, days)} days!")