import json
from core.models import Imagem, Estilo, Promocao, Servico, Regiao, Cor, Tamanho, Cliente

def getEstilos():
    estilos = Estilo.objects.all()
    data = []
    for item in estilos:
        data.append({'estiloId':str(item.idestilo), 'estiloName':str(item.estilo), 'complexidade':item.complexidade})

    return data

def getRegioes():
    R = Regiao.objects.all()
    data = []
    for item in R:
        data.append({'regiaoId':item.idregiao, 'regiaoName':item.regiaodocorpo, 'multiplicador':item.faixavalor})

    return data

def getCores():
    C = Cor.objects.all()
    data = []
    for item in C:
        data.append({'corId':item.idcor, 'corNumber':item.colorido, 'multiplicador':item.faixavalor})

    return data

def getTamanhos():
    T = Tamanho.objects.all()
    data = []
    for item in T:
        data.append({'tamanhoId':item.idtamanho, 'tamanhoName':item.tamanho, 'multiplicador':item.faixavalor})

    return data



def alterarEstilo(imgId,estiloId):
    imgDB = Imagem.objects.get(pk=imgId)
    newEstilo = Estilo.objects.get(idestilo=estiloId).estilo
    if Imagem.objects.filter(pk=imgId).values('idestilo') == 'NULL':
        if imgDB.idestilo != newEstilo:
            Imagem.objects.filter(pk=imgId).update(idestilo=estiloId)
    else:
        Imagem.objects.filter(pk=imgId).update(idestilo=estiloId)

def getAllImages():
    fotos = []
    imagens = Imagem.objects.all().exclude(idestilo=False)
    for item in imagens:
        idImg = item.idimagem
        urlImg = item.urlimagem
        fotos.append({'id': idImg, 'url': urlImg})
    return fotos

def registerService(data):
    msg = ''
    service = data
    client = Cliente.objects.get(idcliente=service['clientId'])
    image = Imagem.objects.get(idimagem=service['imageId'])
    color = Cor.objects.get(idcor=service['colorId'])
    size = Tamanho.objects.get(idtamanho=service['sizeId'])
    local = Regiao.objects.get(idregiao=service['localId'])
    valueOff = None
    if service['promotion']:
        valueOff = Promocao.objects.get(idpromo=service['promotionId']).desconto
    try:
        S = Servico.objects.create(idcliente=client, idimagem=image, idcor=color, idtamanho=size, idregiao=local, servicodesconto=valueOff, servicofinalizado=False)
        S.save()
        msg = 'Serviço Registrado'
    except Exception as e:
        msg = str(e)

    return msg