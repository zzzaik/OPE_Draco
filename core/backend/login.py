from core.backend.criptografia import compararSenha
from core.models import Usuario
import re

def verifyEmail(email):
    return not re.match(r"^([a-zA-Z0-9._-])+@(([a-zA-Z.-])+.)+([a-zA-Z0-9]{2,4})+$", email)

def logar(login, password):
    user = Usuario.objects.filter(loginusuario=login)
    if verifyEmail(login):
        return 'Digite um E-mail Válido!'
    if not user:
        return 'E-mail ou senha incorretos!'
    if compararSenha(password, user[0].senhausuario):
        return ''
    return 'E-mail ou senha incorretos!'

'''
########################Raw sem models##############################################################################
#from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute('SELECT idUsuario, loginUsuario, tipoUsuario FROM Usuario')
    logins = cursor.fetchone()
    return logins

    cursor = connection.cursor()
    cursor.execute('SELECT idUsuario, loginUsuario, tipoUsuario FROM Usuario WHERE %s=%s' %(campo, valor))
    logins = cursor.fetchone()
    return logins

    retorno = (1, 'tatuador@tattoo.com', '0')
'''