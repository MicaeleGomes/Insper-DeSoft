import math

def calcula_area_do_pentagono (l): 
    tangete = math.tan(math.pi/5)
    areaPentagono = (5 * l **2) / ( 4 * tangete )
    return areaPentagono
