from core.Backend.criptografia import compararSenha, cript
from core.models import Usuario

def salvaUsuario(login, password, re_password, salt, tipo):
    user = Usuario.objects.filter(loginusuario=login)
    msg = ''
    if user:
        msg += "Login já registrado! "
    else:
        if password == re_password and compararSenha(password, cript(re_password, salt)):
            user = Usuario.objects.create(loginusuario=login, senhausuario=cript(password, salt), tipousuario=tipo)
            user.save()
            return True
        else:
            msg += "Senhas não batem! "
    return msg