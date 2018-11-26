import requests as req
from core.models import Imagem, Tag, Estilo
'''
def getImages(): #Usando a api v3 em beta provavalmete teremos que atualizar depois
    url = "https://api.pinterest.com/v3/pidgets/users/justinotattoo/pins/"
    ret = req.api.get(url).json()
    return ret
'''
def getMyPins():
    url = "https://api.pinterest.com/v1/me/pins/?access_token=AqWjsuMFTl7lLNgJMAx16tNZruZuFVLHC7vvSIBFNXsqJoAzTAgKgDAAAUufRTl10J_gNhwAAAAA&fields=board%2Cimage%2Cid%2Ccounts%2Cmetadata%2Cnote%2Curl"
    ret = req.api.get(url).json()
    try:
        return ret['data']
    except:
        return ''

def getBoards():
    url = "https://api.pinterest.com/v1/me/boards/?access_token=AqWjsuMFTl7lLNgJMAx16tNZruZuFVLHC7vvSIBFNXsqJoAzTAgKgDAAAUufRTl10J_gNhwAAAAA"
    ret = req.api.get(url).json()
    return ret


#fonteimagem = True(Instagram) / False(Pinterest)
def atualizarCatalogo():
    pins = getMyPins()
    tag = Tag.objects.get(tag='catalogo')
    msg = pins
    #if pins == '': #Verificação para quando a api dar maxRequestReached
    #    return pins
    for pin in pins:
        imagem = pin['image']['original']['url']
        try:
            img = Imagem.objects.create(urlimagem=imagem, ratins=0, idestilo=None, fonteimagem=False, idtag=tag)
            img.save()
            msg = 'Imagens Salvas'
        except Exception as e:
            msg = str(e)
    return msg

def selectPins():
    pins = {'classf':[],'noClassf':[]}
    tag = Tag.objects.get(tag='catalogo')
    imgClass = tag.imagem_set.exclude(idestilo=False)
    imgNoClass = tag.imagem_set.filter(idestilo__isnull=True)

    for foto in imgClass:
        imgId = foto.idimagem
        urlImg = foto.urlimagem
        styleId = str(foto.idestilo)
        pins['classf'].append({'imgId':imgId, 'url':urlImg, 'estiloId':styleId})

    for foto in imgNoClass:
        imgId = foto.idimagem
        urlImg = foto.urlimagem
        pins['noClassf'].append({'imgId':imgId, 'url':urlImg, 'estiloId':"---"})

    return pins

def alocarPins():
    pins = []
    tag = Tag.objects.get(tag='catalogo')
    imgClass = tag.imagem_set.exclude(idestilo=False)


    for pin in imgClass:
        imgId = pin.idimagem
        urlImg = pin.urlimagem
        styleId = str(pin.idestilo)
        complexidade = Estilo.objects.get(estilo=styleId).complexidade
        pins.append({'imageId':imgId, 'url':urlImg, 'estiloId':styleId, 'estiloComplex':complexidade})
    return pins


''' retorno da imagem em getMyPints()
{'data': [{'url': 'https://www.pinterest.com/pin/579416308285316876/',
'image': {'original': {'url': 'https://i.pinimg.com/originals/b7/ee/92/b7ee922745036686d13eff26b16dd927.jpg', 'width': 899, 'height': 1599}},
'note': 'Arte', 'board': {'url': 'https://www.pinterest.com/zzzaik/pasta-teste/', 'id': '579416376998086390', 'name': 'Pasta Teste'},
'counts': {'saves': 0, 'comments': 0}, 'id': '579416308285316876', 'metadata': {}}, {'url': 'https://www.pinterest.com/pin/579416308285193447/',
'image': {'original': {'url': 'https://i.pinimg.com/originals/9e/47/73/9e4773718a1439a3241e929c243b6f04.jpg', 'width': 474, 'height': 705}},
'note': "Rick and Morty e Dungeons & Dragons | Crossover acontecerá em série de HQ's", 'board': {'url': 'https://www.pinterest.com/zzzaik/pasta-teste/',
'id': '579416376998086390', 'name': 'Pasta Teste'}, 'counts': {'saves': 0, 'comments': 0}, 'id': '579416308285193447',
'metadata': {'article': {'published_at': '2018-04-10T00:00:00',
'description': 'Foi anunciado no último final de semana durante a Chicago Comic & Entertainment Expo, um crossover entre Rick and Morty e Dungeons & Dragons.', 'name': 'Rick and Morty e Dungeons & Dragons', 'authors': []}, 'link': {'locale': 'pt_BR', 'title': "Rick and Morty e Dungeons & Dragons | Crossover acontecerá em série de HQ's",
'site_name': 'Geek Project', 'description': 'Foi anunciado no último final de semana durante a Chicago Comic & Entertainment Expo, um crossover entre Rick and Morty e Dungeons & Dragons.',
'favicon': 'https://i.pinimg.com/favicons/53a70c4fef67bbb8c39e0fb4a3bcf730ef8a774c83275cbbfe1da135.png?47bb958e796c697f26abed072400345f'}}}]}
'''
