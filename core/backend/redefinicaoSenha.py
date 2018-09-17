from core.models import Usuario
from core.backend.criptografia import cript, compararSenha
from core.backend.token import excluirToken

def alterarSenha(login, password, re_password, salt):
    user = Usuario.objects.filter(loginusuario=login)
    if user[0].econfiavel == 0:
        return 'Você não confirmou o e-mail, não pode alterar a senha!'
    if password == re_password and compararSenha(password, cript(re_password, salt)):
        user.update(senhausuario=cript(password, salt))
        excluirToken(login)
        return ''
    return 'As senhas não batem!'





