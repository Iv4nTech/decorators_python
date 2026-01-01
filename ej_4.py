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