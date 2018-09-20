from core.backend.criptografia import compararSenha, cript
from core.models import Usuario
import re

def verifyEmail(email):
    return not re.match(r"^([a-zA-Z0-9._-])+@(([a-zA-Z.-])+.)+([a-zA-Z0-9]{2,4})+$", email)


def salvaUsuario(login, password, re_password, salt=8, tipo=False):
    user = Usuario.objects.filter(loginusuario=login)
    msg = ''
    if user:
        msg += "Login já registrado! "
    elif verifyEmail(login):
        msg += "Digite um e-mail válido! "
    else:
        if password == re_password and compararSenha(password, cript(re_password)):
            user = Usuario.objects.create(loginusuario=login, senhausuario=cript(password), tipousuario=tipo, econfiavel=False)
            user.save()
            return True
        else:
            msg += "Senhas não batem! "
    return msg