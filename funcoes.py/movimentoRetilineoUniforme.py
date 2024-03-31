''''
Faça uma função que calcule a posição de um objeto em movimento retilíneo uniforme em um instante t, com posição inicial S0 e velocidade v:

S = f(t, S0, v) = S0 + v * t

O nome da sua função deve ser calcula_posicao
'''

def calcula_posicao (tempo, posicaoIncial,velocidade):
    
    posicao = posicaoIncial + (velocidade * tempo)

    return posicao