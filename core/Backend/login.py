from core.Backend.criptografia import compararSenha
from core.models import Usuario

def getLogins(self):
    logins = {}
    for (id, login, tipo) in Usuario.objects.raw('SELECT idUsuario, loginUsuario, Tipo FROM Usuarios'):
        logins[id] = {
            'login':login,
            'tipo':tipo
        }
    return logins #Lista de logins do banco (usando a classe USERS do MODEL.py)


def verificaLogin(login, password, passowordHashed):
    logins = getLogins()
    for x in logins:
        print(x)
    if login in logins and compararSenha(password, passowordHashed):
        pass


