# Crea un decorador auditoria que imprima 
# el nombre de la función ejecutada y los valores de los argumentos recibidos (*args y **kwargs) cada vez que se llame a la función.

import functools

def auditoria(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print(f"Nombre de la función ejecutada: {function.__name__}")
        print(f'Parámetros de la función: {(args or kwargs)}')
    return wrapper
    
@auditoria
def saludo(mensaje):
    print('Hola, mundo!', mensaje)

saludo('hola caracola')