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
            return sum(args) + sum(kwargs)
       else:
           print('Cacheado!') 
           print(parametros_guardados)
           return sum(list(parametros_guardados[parametros_guardar].keys())[0])
    return wrapper

@memorizar
def sumar(*args):
    return sum(args)

#Para mostrar los números, para ver que verdaderamente se están sumando
resultado = sumar(5, 5)
print('Resultado:', resultado, sep=" ")

resultado = sumar(5, 5)
print('Resultado:', resultado, sep=" ")