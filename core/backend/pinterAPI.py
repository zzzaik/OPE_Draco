import requests as req
from core.models import Imagem
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
def salvarPins():
    pins = getMyPins()
    msg = ''
    if pins == '': #Verificação para quando a api dar maxRequestReached
        return pins
    for pin in pins:
        imagem = pin['image']['original']['url']
        try:
            img = Imagem.objects.create(urlimagem=imagem, ratins=None, idestilo=None, idtag=1, fonteimagem=False)
            img.save()
            msg += ''
        except:
            msg += 'Imagem já salva! '
    return msg

def selectPins(imgs=0):
    pins = {}
    resp = getMyPins()
    if resp == '': #Verificação para quando a api dar maxRequestReached
        return resp
    cont = 0
    if imgs == 0:
        for elements in resp:
            pins[cont] = elements['image']['original']['url']
            cont += 1
        return pins
    elements = resp
    while cont < imgs:
        pins[cont] = elements[cont]['image']['original']['url']
        cont += 1
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
