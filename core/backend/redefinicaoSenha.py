from core.models import Token, Usuario
from core.backend.criptografia import cript, compararSenha

def alterarSenha(login, password, re_password, salt):
    user = Usuario.objects.filter(loginusuario=login)
    if user[0].econfiavel == 0:
        return 'Você não confirmou o e-mail, não pode alterar a senha!'
    if password == re_password and compararSenha(password, cript(re_password, salt)):
        user.update(senhausuario=cript(password, salt))
        token = Token.objects.filter(idusuario=user[0].idusuario)
        token.update(ativo=0)
        return ''
    return 'As senhas não batem!'





