from core.models import Usuario
from core.backend.token import excluirToken

def tornarConfiavel(login):
    Usuario.objects.filter(loginusuario=login).update(econfiavel=True)
    excluirToken(login)