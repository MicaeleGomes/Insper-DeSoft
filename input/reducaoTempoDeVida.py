# Escreva um programa que calcule a redução de tempo de vida de um fumante a partir do número de cigarros.
# Pergunte quantos cigarros ele fuma por dia e há quantos anos fuma e imprima o tempo de vida perdido em dias.
# Considere que um cigarro rouba 10 minutos de expectativa de vida.

cigarros_por_dia = int(input("Quantos cigarros você fuma por dia?: "))

anos_fumando = int(input("Há quantos anos você fuma?: "))

tempo_dia = (cigarros_por_dia * 10) / 1440
tempo_anos = anos_fumando * 365

tempo_total_perdido = (tempo_dia * tempo_anos)

print (tempo_total_perdido)
