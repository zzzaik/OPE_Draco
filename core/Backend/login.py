from core.Backend.criptografia import compararSenha

def getEmails():
    return {b'123': b'$2b$08$qK1TxrDh9z9df3DqEi2HyeLHm/58grEkOutD/dK7I38.WDw.24xum'}#Lista de logins do banco (usando a classe USERS do MODEL.py)

def verificaLogin(email, password, passowordHashed):
    emails = getEmails()
    if email in emails and comparaSenha(password, passowordHashed):
        pass