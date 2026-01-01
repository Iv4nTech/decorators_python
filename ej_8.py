# Crea un decorador memoizar que guarde en un diccionario los resultados de funciones costosas basados en sus argumentos.
# Si se llama a la función con los mismos argumentos, debe devolver el valor guardado en lugar de recalcularlo.

parametros_guardados = {}

def memorizar(function):
    def wrapper(*args, **kwargs):
       parametros_guardar = args + tuple(kwargs.items())
       if parametros_guardar not in parametros_guardados:
            parametros_guardados[parametros_guardar] = parametros_guardados
            print('Calculando...')
            print(parametros_guardados)
            return parametros_guardados
       else:
           print('Cacheado!')
           print(parametros_guardados)
           return parametros_guardados
    return wrapper

@memorizar
def sumar(*args):
    return sum(args)

sumar(1,4,5,4)
sumar(1,4,3,4)
sumar(1,4,5,4)
sumar(1,4,5,4)
