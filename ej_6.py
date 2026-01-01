# Crea un decorador llamado repetir(n) que reciba un número entero n como parámetro y ejecute la función decorada n veces.

def repeticiones(veces):
    def repetir(function):
        def wrapper():
            for i in range(veces):
                function()
        return wrapper
    return repetir

@repeticiones(10)
def saludar():
    print('hola mundo')

saludar()