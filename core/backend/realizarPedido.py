from core.models import Usuario, Cliente

def verificarCliente(request, login):
    user = Usuario.objects.filter(loginusuario=login)
    if user:
        pass
    return True
