def createSession(request, session, value=""):
    if request.session.get(session) is None:
        request.session[session] = value
    return request.session.get(session)

def alterSession(request, session, value=""):
    s = createSession(request, session)
    if s != value:
        s[session] = value
    return s

def verifyUserSession(request):
    if request.session.get('user') is None:
        request.session['user'] = {'login':'','nome':'','tipo':'', 'confiavel':'','auth':False}
    return request.session.get('user')

def isLogged(request):
    verifyUserSession(request)
    return request.session['user']['auth'] #retorna True quando o usuario está autentucado e False quando não está

def redefSenhaSession(request, login):
    if request.session.get('login') is None:
        request.session['login'] = login
    return request.session.get('login')

def killSession(request, session):
    if request.session.get(session) is not None:
        del request.session[session]