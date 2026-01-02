from colorama import Fore
import functools 

#BIEN HECHO
texto_usuario = input('Escribe lo que quieras:')

def colorear_rojo(funcion):
    @functools.wraps(funcion)
    def wrapper(texto):
        return Fore.RED + texto
    return wrapper
@colorear_rojo
def mensaje(texto):
    return texto

resultado = mensaje(texto_usuario)
print(resultado)

#MAL HECHO (Porque no va a ser reutilizable y vamos a tener que repetir codigo)
from colorama import Fore

texto_usuario = input('Escribe lo que quieras: ')

def mensaje(texto):
    return Fore.RED + texto 

resultado = mensaje(texto_usuario)
print(resultado)

