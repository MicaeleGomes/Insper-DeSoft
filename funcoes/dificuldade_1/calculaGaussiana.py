import math 

def calcula_gaussiana (x, mi, sigma): 
    parte1 = math.sqrt(2 * math.pi)
    parte2 = 1/(sigma * parte1)    
    parte3 = ((x - mi) / sigma)**2
    parte4 = (-0.5 * parte3)

    gaussiana = parte2 * math.e ** parte4

    return gaussiana
