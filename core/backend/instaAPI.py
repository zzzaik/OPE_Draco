import requests as req
from core.models import Imagem, Tag, Imagemtag, Estilo

def getFoto():
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=3251373559.1556bce.467e8e9f0219425abf9915fa978bb275"
    ret = req.api.get(url).json()
    return ret

def salvarFoto(estiloEscolhido=None):
    fotos = getFoto()
    msg = ''
    for foto in fotos['data']:
        imagem = foto['images']['standard_resolution']['url']
        likes = foto['likes']['count']
        est = Estilo.objects.only('idestilo').get(estilo=estiloEscolhido)
        if est:
            try:
                img = Imagem.objects.create(urlimagem=imagem, ratins=likes, idestilo=est, fonteimagem=True)
                img.save()
                msg += ''
            except:
                msg += 'Imagem já salva! '
        else:
            msg += 'Estilo não encontrado! '
    return msg

def selectFotos(estilo=None,tamanho=None,cor=None,regiao=None):
    fotos = []
    img = Imagem.objects.all()

    for foto in img:
        fotos.append({'url':foto.urlimagem,'estilo':foto.idestilo})

    return fotos

'''
def alterarEstilo(imagem, estilo):
    img = Imagem.objects.filter(idimagem=imagem)
    img.update(estilo=Estilo.objects.only('idestilo').get(estilo=estilo))
'''

def alocarFotos(imgs=0):
    fotos = {}
    resp = getFoto()
    cont = 0
    if imgs == 0:
        for elements in resp['data']:
            fotos[cont] = elements['images']['standard_resolution']['url']
            cont += 1
        return fotos
    else:
        elements = resp['data']
        while cont < imgs:
            fotos[cont] = elements[cont]['images']['standard_resolution']['url']
            cont += 1
        return fotos