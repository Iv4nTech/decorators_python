# Escribe un decorador requiere_rol(rol_permitido). La función decorada debe recibir un diccionario de usuario. Si el rol del 
# usuario no coincide con el rol_permitido, debe mostrar "Acceso Denegado".

roles_permitidos = ['Coronel', 'Comandante', 'Soldado']
rol_user = input('¿Cuál es su rol?')

def requiere_rol(rol):
    def comprobar(function):
        def wrapped(*args, **kwargs):
            if rol_user not in roles_permitidos:
                print('Acceso denegado')
            else:
                print('Acceso permitido!')
                function()
        return wrapped
    return comprobar
        
@requiere_rol(rol_user)
def rol_comprobar():
    print('Tiene los permisos, muy bien soldado!')

rol_comprobar()




