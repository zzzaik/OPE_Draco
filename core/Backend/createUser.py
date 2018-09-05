from core.Backend.criptografia import compararSenha
#from coneccaoBanco import getLogins

def getLogins():
    return {b'123': b'$2b$08$qK1TxrDh9z9df3DqEi2HyeLHm/58grEkOutD/dK7I38.WDw.24xum'}#Lista de logins do banco (usando a classe USERS do MODEL.py)

def verificaLogin(login):
    logins = getLogins()
    if login not in logins:
        return ''
    return "Login já registrado!"


def verificaSenha(password, re_passwordHashed):
    if compararSenha(password, re_passwordHashed):
        return ''
    return "As senhas não batem!"

def gravaUsuario(login, passwordHashed):
    try:
        logins = getLogins()
        logins[login] = passwordHashed
        print(logins)
    except:
        return False