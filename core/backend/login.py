from core.backend.criptografia import compararSenha
from core.models import Usuario

#from django.db import connection, transaction

def logar(login, password):
    user = Usuario.objects.filter(loginusuario=login)
    if not user:
        return [False, False, 'E-mail ou senha incorretos!']
    if compararSenha(password, user[0].senhausuario):
        return [True, user[0].tipousuario, '']
    return [False, False, 'E-mail ou senha incorretos!']

def getUsuarios(): #se for usar o raw sem models usar (campo, valor)
    values_list = Usuario.objects.values_list('idusuario', 'loginusuario', 'senhausuario', 'tipousuario') #para chamar so 1 valor usar flat=True
    Lvalues_list = {}
    for id, login, senha, tipo in values_list:
        Lvalues_list[id] = (id, login, senha, tipo)
    return Lvalues_list

'''
#######################Raw com models##############################################################################
    logins = {}
    for id, login, tipo in Usuario.objects.raw('SELECT idUsuario, loginUsuario, tipoUsuario FROM Usuario'):
        logins[id] = {
            'login':login,
            'tipo':tipo
        }
    return logins

    Não ta funcionando
########################Raw sem models##############################################################################
    cursor = connection.cursor()
    cursor.execute('SELECT idUsuario, loginUsuario, tipoUsuario FROM Usuario')
    logins = cursor.fetchone()
    return logins

    cursor = connection.cursor()
    cursor.execute('SELECT idUsuario, loginUsuario, tipoUsuario FROM Usuario WHERE %s=%s' %(campo, valor))
    logins = cursor.fetchone()
    return logins

    retorno = (1, 'user1@tattoo.com', 't')
########################Usando o models do django###################################################################
    values_list = Usuario.objects.values_list('idusuario', 'loginusuario', 'tipousuario') #para chamar so 1 valor usar flat=True
    Lvalues_list = {}
    for id, login, tipo in values_list:
        Lvalues_list[id] = {
            'login':login,
            'tipo':tipo
        }
    return Lvalues_list

    retorno {1: {'login': 'user1@tattoo.com', 'tipo': 't'}, 2: {'login': 'user2@tattoo.com', 'tipo': 'c'}}
########################Incerir no banco############################################################################
u = Usuario.objects.create(loginusuario='user2@tattoo.com', senhausuario='$2y$08$3fngEOGMtokozZroCEOasOqQMcxoVZJ5bHfqkLPFnVtlUQXsnZvG', tipousuario='c')
   u.save()
'''