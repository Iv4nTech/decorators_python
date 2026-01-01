# Escribe un decorador solo_enteros que verifique que todos los argumentos pasados a una función sean de tipo int. 
# Si algún argumento no lo es, debe lanzar una excepción o imprimir un error en lugar de ejecutar la función.

import functools

def solo_enteros(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        for num in args:
            if not isinstance(num, int): #Comprobamos los parametros que todos sean tipo int, si uno no es se ejecutara el raise
                raise ValueError('El usuario ha introducido tipo de dato que no es un entero')
        funcion(*args, **kwargs)
    return wrapper

@solo_enteros
def funcion_ejemplo(*args):
    print(f'Los numeros que se han introducido en la funcion: {args}')

funcion_ejemplo(10, 9, 8, 7, 'hola')

print(funcion_ejemplo.__name__)