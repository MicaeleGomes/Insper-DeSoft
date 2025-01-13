# Faça uma função que recebe 4 números, x1, y1, x2, y2, e retorna a distância entre os 
# pontos (x1, y1) e (x2, y2). Sua função deve se chamar distancia_euclidiana.

import math

def distancia_euclidiana (x1, y1, x2,y2): 

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distancia 
