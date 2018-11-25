import requests as req
import random
from core.models import Imagem, Promocao, PromoImagem

def newPromo(data):
    desc = data['desconto']
    msg = ''
    try:
        P = Promocao.objects.create(desconto=desc, ativo=True)
        P.save()
        msg = 'Promoção Salva'
    except Exception as e:
        msg = str(e)
    return msg

def registerPromo(data):
    idP = Promocao.objects.get(idpromo=data['promoId'])
    dataVal = data['validade']
    msg = ''
    for item in data['imagens']:
        idI = Imagem.objects.get(idimagem=item['imagemId'])
        try:
            PI = PromoImagem(idpromo=idP, idimagem=idI, validade=dataVal)
            PI.save()
            msg = 'Imagens Salvas em Promoção'
        except Exception as e:
            msg = str(e)

    return msg

def getPromos():
    promocoes = []
    promosDB = Promocao.objects.all()
    for p in promosDB:
        imagens = []
        imagensDB = PromoImagem.objects.all().filter(idpromo=p.idpromo).values('idimagem')
        for i in imagensDB:
            idImg = i['idimagem']
            url = Imagem.objects.get(idimagem=idImg).urlimagem
            imagens.append(url)
        promocoes.append({'idPromo':p.idpromo, 'desconto':int(p.desconto*100), 'ativo': p.ativo, 'imagens': imagens})
    return promocoes

def getPromoImages():
    imagens = []
    promosDB = Promocao.objects.all()
    for p in promosDB:
        imagensDB = PromoImagem.objects.all().filter(idpromo=p.idpromo).values('idimagem')
        for i in imagensDB:
            idImg = i['idimagem']
            url = Imagem.objects.get(idimagem=idImg).urlimagem
            imagens.append({'idPromo':p.idpromo, 'url':url})
    return imagens

def showPromos():
    promocoes = []
    promosDB = Promocao.objects.all().filter(ativo=True)
    for p in promosDB:
        imagensDB = PromoImagem.objects.all().filter(idpromo=p.idpromo).values('idimagem')
        for i in imagensDB:
            idImg = i['idimagem']
            url = Imagem.objects.get(idimagem=idImg).urlimagem
            promocoes.append({'desconto':int(p.desconto*100), 'url': url})
    return promocoes