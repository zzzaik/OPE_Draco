import requests as req
from core.models import Tag, Imagem, Estilo

def getFoto():
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=3251373559.1556bce.467e8e9f0219425abf9915fa978bb275"
    ret = req.api.get(url).json()
    return ret

def atualizarPortifolio():
    fotos = getFoto()
    tag = Tag.objects.get(tag='portifolio')
    msg = ''
    for foto in fotos['data']:
        imagem = foto['images']['standard_resolution']['url']
        likes = foto['likes']['count']
        try:
            img = Imagem(urlimagem=imagem, ratins=likes, idestilo=None, fonteimagem=True, idtag=tag)
            img.save()
            msg = 'Imagens Salvas'
        except Exception as e:
            msg = str(e)
    return msg


def selectFotos():
    fotos = {'classf':[],'noClassf':[]}
    tag = Tag.objects.get(tag='portifolio')
    imgClass = tag.imagem_set.exclude(idestilo=False)
    imgNoClass = tag.imagem_set.filter(idestilo__isnull=True)

    for foto in imgClass:
        imgId = foto.idimagem
        urlImg = foto.urlimagem
        styleId = str(foto.idestilo)
        fotos['classf'].append({'imgId':imgId, 'url':urlImg, 'estiloId':styleId})

    for foto in imgNoClass:
        imgId = foto.idimagem
        urlImg = foto.urlimagem
        fotos['noClassf'].append({'imgId':imgId, 'url':urlImg, 'estiloId':"---"})

    return fotos

def alocarFotos():
    fotos = []
    tag = Tag.objects.get(tag='portifolio')
    imgClass = tag.imagem_set.exclude(idestilo=False)

    for foto in imgClass:
        imgId = foto.idimagem
        urlImg = foto.urlimagem
        styleId = str(foto.idestilo)
        complexidade = Estilo.objects.get(estilo=styleId).complexidade
        fotos.append({'imageId':imgId, 'url':urlImg, 'estiloId':styleId, 'estiloComplex':complexidade})
    return fotos

def getRecentes():
    fotos = []
    tag = Tag.objects.get(tag='portifolio')
    imgClass = tag.imagem_set.exclude(idestilo=False).order_by('-idimagem')

    for x in range(0,8):
        imgId = imgClass[x].idimagem
        urlImg = imgClass[x].urlimagem
        fotos.append({'imgId':imgId, 'url':urlImg})
    return fotos

def getTop5():
    fotos = []
    tag = Tag.objects.get(tag='portifolio')
    imgClass = tag.imagem_set.exclude(idestilo=False).order_by('-ratins')

    for x in range(0,5):
        imgId = imgClass[x].idimagem
        urlImg = imgClass[x].urlimagem
        rating = imgClass[x].ratins
        fotos.append({'imgId':imgId, 'url':urlImg, 'rating':rating, 'pos':x})
    return fotos