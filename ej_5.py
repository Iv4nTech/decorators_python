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