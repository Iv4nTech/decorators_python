# Crea un decorador llamado medir_tiempo que utilice el módulo time. Debe imprimir cuánto tiempo tarda en ejecutarse la función decorada.

from time import sleep, time
# Permite es módulo usar functools.wraps
import functools

#Creación del decorador
def medir_tiempo(funcion):
    # Conseguimos que la función original mantenga los metadatos que tiene y no los del wrapper
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        tiempo_inicial = time()
        sleep(3)
        funcion()
        sleep(0.5)
        tiempo_final = time()
        print(f'El tiempo que ha tardado en ejecutarse es: {tiempo_final - tiempo_inicial}')
    return wrapper

#Invoación del decorador
@medir_tiempo
def funcion_base():
    '''Hola, esto es un comentario muy chulo'''
    print('EJECUTADA!')

funcion_base()

# Nombre de la función original, si quitamos functools.wraps el nombre de la funcion que saldría es la de wrapper
print(funcion_base.__name__)
print(funcion_base.__doc__)