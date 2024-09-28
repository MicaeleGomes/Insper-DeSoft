# Escreva um programa que pergunte, em sequência, uma quantidade de dias, horas, minutos e segundos para o usuário. Depois calcule o total em segundos e imprima.

# Obs. quando for rodar os testes só imprima o número de segundos e nada mais.

dias = int(input("Quantidade de dias?: "))
horas = int(input("Quantidade de horas?: "))
minutos = int(input("Quantidade de minutos?: "))
segundos = int(input("Quantidade de segundos?: "))

total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print(total_segundos)
