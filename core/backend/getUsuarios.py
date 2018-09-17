from core.models import Usuario

def getUsuarios(): #se for usar o raw sem models usar (campo, valor)
    values_list = Usuario.objects.values_list('idusuario', 'loginusuario', 'senhausuario', 'tipousuario') #para chamar so 1 valor usar flat=True
    Lvalues_list = {}
    for id, login, senha, tipo in values_list:
        Lvalues_list[id] = (id, login, senha, tipo)
    return Lvalues_list