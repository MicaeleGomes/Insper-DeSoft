# Faça uma função que calcula a posição de um corpo em movimento retilíneo uniformemente variado. Ou seja, faça uma função que calcula o valor S tal que:
# S = S0 + V0 * t + ((a * t^2) / 2)

# Onde:
# S0 é a posição inicial, V0 é a velocidade inicial, a é a aceleração linear e t é o tempo decorrido. 
# A função deve receber os argumentos na ordem: posição inicial, velocidade inicial, aceleração e tempo decorrido.

# Sua função deve se chamar calcula_posicao.

def calcula_posicao (p0,v0,a,t): 
    posicao = p0 + v0 * t + ((a * t**2)/2)
    return posicao
