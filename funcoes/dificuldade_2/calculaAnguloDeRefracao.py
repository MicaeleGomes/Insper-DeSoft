# A lei de Snell-Descartes define que a relação entre o ângulo de incidência e o ângulo de refração de um raio de luz 
# atravessando de um meio para o outro é inversamente proporcional a razão dos índices de refração dos meios, que é dado pela seguinte fórmula:

# n1/n2 = sen(theta2) / sen(theta1)

# Faça uma função que recebe os valores de n1, n2 e theta1 e retorna o valor do theta2. Os valores passados de n1, n2, 
# são adimensionais, já os valores de theta1 e theta2 deverão ser recebidos e retornados em graus.

# Sua função deve se chamar snell_descartes.

import math 

def snell_descartes(n1, n2, O1):

    O1_radianos = math.radians(O1)

    sin_O2 = (n1/n2) * math.sin(O1_radianos)

    # Calcular O2 em radianos usando o arc-seno (inversa do seno)
    O2_radianos = math.asin(sin_O2)

    # Converter O2 de radianos para graus
    O2 = math.degrees(O2_radianos)
    
    return O2

    
