from core.templatestag.Backend.criptografia import compararSenha
from core.models import Users

def getEmails():
    return {b'123': b'$2b$08$qK1TxrDh9z9df3DqEi2HyeLHm/58grEkOutD/dK7I38.WDw.24xum'}#Lista de logins do banco (usando a classe USERS do MODEL.py)

def verificaEmail(email):
    emails = getEmails()
    if email not in emails:
        return ''
    return "Email já registrado!"


def verificaSenha(password, re_passwordHashad):
    if compararSenha(password, re_passwordHashad):
        return ''
    return "As senhas não batem!"

def gravaUsuario(email, passwordHashed):
    try:
        emails = getEmails()
        emails[email] = passwordHashed
        print(emails)
    except:
        return False