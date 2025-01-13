# Escreva uma função que recebe um número, representando um ano, e retorna True se o ano é bissexto e False caso contrário.
# Sua função deve se chamar eh_bissexto.

def eh_bissexto (numero): 

    if numero % 400 == 0:
        return True

    elif numero % 100 == 0: 
        return False

    elif numero % 4 == 0:
        return True

    else: 
        return False
