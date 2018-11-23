import requests as req
from core.models import Tag, Imagem, Estilo

def getFoto():
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=3251373559.1556bce.467e8e9f0219425abf9915fa978bb275"
    ret = req.api.get(url).json()
    return ret

def atualizarCatalogo():
    fotos = getFoto()
    tag = Tag.objects.get(tag='catalogo').idtag
    msg = ''
    for foto in fotos['data']:
        imagem = foto['images']['standard_resolution']['url']
        likes = foto['likes']['count']
        try:
            img = Imagem(urlimagem=imagem, ratins=likes, idestilo=None, fonteimagem=True)
            img.save()
            msg = 'Imagens Salvas'
        except Exception as e:
            msg = str(e)
        imgSave = Imagem.objects.get(urlimagem=imagem)
        imgSave.idtag = tag
        imgSave.save()
    return msg


def alterarEstilo(imgId,estiloId):
    imgDB = Imagem.objects.get(pk=imgId)
    newEstilo = Estilo.objects.get(idestilo=estiloId).estilo
    if Imagem.objects.filter(pk=imgId).values('idestilo') == 'NULL':
        if imgDB.idestilo != newEstilo:
            Imagem.objects.filter(pk=imgId).update(idestilo=estiloId)
    else:
        Imagem.objects.filter(pk=imgId).update(idestilo=estiloId)


def selectFotos():
    fotos = {'classf':[],'noClassf':[]}
    tag = Tag.objects.filter(tag='catalogo')
    imgNoClass = tag.imagem_set.objects.all().filter(idestilo__isnull=True)
    imgClass = tag.imagem_set.objects.all().exclude(idestilo=False)


    for foto in imgClass:
        imgId = foto.idimagem
        urlImg = foto.urlimagem
        styleId = str(foto.idestilo)
        fotos['classf'].append({'imgId':imgId, 'url':urlImg, 'estilo':styleId})

    for foto in imgNoClass:
        imgId = foto.idimagem
        urlImg = foto.urlimagem
        fotos['noClassf'].append({'imgId':imgId, 'url':urlImg, 'estilo':"---"})

    return fotos

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
