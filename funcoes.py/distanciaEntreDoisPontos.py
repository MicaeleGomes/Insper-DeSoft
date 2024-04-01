''''
Faça uma função que recebe 4 números, x1, y1, x2, y2, e devolve a distância entre os pontos (x1,y1) e (x2,y2).
O nome da sua função deve ser distancia_euclidiana
'''

#Fórmula: dAB = √((x1 – x2)² + (y1 – y2)²)

import math

def distancia_euclidiana (x1,y1, x2,y2):
    distanciaA_B = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

    return distanciaA_B