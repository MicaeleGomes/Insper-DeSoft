import math

def calcula_distancia_do_projetil(v, angulo,yo): 
    g = 9.8
    raiz = math.sqrt(1 + (2 * g * yo) / (v**2 * (math.sin(angulo)**2)))
    distancia = ((v**2)/(2 * g)) * (1 + raiz) * math.sin(2 * angulo)
    return distancia
