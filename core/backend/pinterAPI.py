import requests as req

def getImages(): #Usando a api v3 em beta provavalmete teremos que atualizar depois
    url = "https://api.pinterest.com/v3/pidgets/users/justinotattoo/pins/"
    ret = req.api.get(url).json()
    return ret

def getMyPins():
    url = "https://api.pinterest.com/v1/me/pins/?access_token=AqWjsuMFTl7lLNgJMAx16tNZruZuFVLHC7vvSIBFNXsqJoAzTAgKgDAAAUufRTl10J_gNhwAAAAA"
    ret = req.api.get(url).json()
    return ret

def getMyBoards():
    url = "https://api.pinterest.com/v1/me/boards/?access_token=AqWjsuMFTl7lLNgJMAx16tNZruZuFVLHC7vvSIBFNXsqJoAzTAgKgDAAAUufRTl10J_gNhwAAAAA"
    ret = req.api.get(url).json()
    return ret

def pins(imgs=0):
    pins = {}
    resp = getImages()
    cont = 0
    if imgs == 0:
        for elements in resp['data']['pins']:
            pins[cont] = elements['images']['237x']['url']
            cont += 1
        return pins
    else:
        while cont < imgs:
            print(resp['data']['pins'])
            pins[cont] = resp['images']['237x']['url']
            cont += 1
        return pins

print(pins())
print(pins(4))

