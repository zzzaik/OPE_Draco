def verifySession(request):
    if request.session.get('user') is None:
        request.session['user'] = {'username':'','name':'','type':'','auth':False}
    return request.session.get('user')

def isLogged(request):
    verifySession(request)
    return request.session['user']['auth'] #retorna True quando o usuario está autentucado e False quando não está

def redefSenhaSession(request, login):
    if request.session.get('login') is None:
        request.session['login'] = login
    return request.session.get('login')