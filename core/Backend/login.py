from core.Backend.criptografia import compararSenha
from core.models import Usuario

from django.db import connection#, transaction


def getLogins():
    #cursor = connection.cursor()
    #cursor.execute('SELECT idUsuario, loginUsuario, tipoUsuario FROM Usuario')
    #logins = cursor.fetchone()
    #logins = {}
    #for (id, login, tipo) in Usuario.objects.raw('SELECT idUsuario, loginUsuario, tipoUsuario FROM Usuario'):
    #    logins[id] = {
    #        'login':login,
    #        'tipo':tipo
    #    }
    #return logins #Lista de logins do banco (usando a classe USERS do MODEL.py)
    return Usuario.objects.all()


def verificaLogin(login, password, passowordHashed):
    logins = getLogins()
    if login in logins and compararSenha(password, passowordHashed):
        pass
    return logins
'''
def getLogins():
    pass

def verificaLogin():
    pass
'''