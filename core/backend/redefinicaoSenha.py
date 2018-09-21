from core.models import Usuario
from core.backend.criptografia import cript, compararSenha
from core.backend.token import excluirToken

def alterarSenha(login, password, re_password, salt=8):
    user = Usuario.objects.filter(loginusuario=login)
    if user[0].econfiavel == 0:
        return 'Você não confirmou o e-mail, não pode alterar a senha!'
    if len(password) < 8:
        return 'A senha deve ter no minimo 8 caracteres! '
    if compararSenha(password, user[0].senhausuario):
        return 'A sua nova senha não pode ser igual a senha antiga! '
    if password == re_password and compararSenha(password, cript(re_password)):
        user.update(senhausuario=cript(password, salt))
        excluirToken(login)
        return ''
    return 'As senhas não batem!'

def verificarSenha(login, password):
    user = Usuario.objects.filter(loginusuario=login)
    if compararSenha(password, user[0].senhausuario):
        return ''
    return 'Senha antiga incorreta! '



