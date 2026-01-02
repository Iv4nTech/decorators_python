# Diseña un decorador ejecutar_una_vez que permita que una función se ejecute 
# normalmente la primera vez, pero que en las llamadas subsiguientes no haga nada (o devuelva un mensaje indicando que ya se ejecutó).

def ejecutar_una_vez(function):
    def wrapper():
        if hasattr(wrapper, 'ejecutado'):
            print('Esta función ya no se puede ejecutar')
            return None
        resultado = function()
        print('Función ejecutada')
        wrapper.ejecutado = True
        return resultado
    return wrapper


@ejecutar_una_vez
def saludar():
    print('Hola!')

saludar()
saludar()
saludar()
saludar()
saludar()