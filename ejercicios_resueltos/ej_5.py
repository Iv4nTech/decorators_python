# Crea dos decoradores: en_negrita y en_cursiva. 
# Aplica ambos a una función que devuelva una cadena de texto para que el resultado final esté envuelto en etiquetas (ejemplo: <i><b>Hola</b></i>).

def en_negrita(function):
    def wrapper():
        return f'<b>{function()}<b>'
    return wrapper

def en_cursiva(function):
    def wrapper():
        return f'<i>{function()}<i>'
    return wrapper

@en_negrita
@en_cursiva
def printear_palabras():
    return 'Hola mundo'

print(printear_palabras())