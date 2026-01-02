# Diseña un decorador a_json que tome el 
# diccionario devuelto por una función y lo convierta automáticamente en una cadena de texto en formato JSON (usa el módulo json).

import json

def to_json(function):
    def wrapper(*args, **kwargs):
            resultado = function()
            str_convertido = json.dumps(resultado, indent=4, ensure_ascii=False)
            return str_convertido
    return wrapper

@to_json
def crear_dict():
    dict1 = {'hola':1, 'adios':0, 'alumnos': {'Alumno1': 'pepe'}}
    return dict1

print(crear_dict())