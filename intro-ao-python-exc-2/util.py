import json

def carregarDados():
    file = open('clientes.txt', 'r')
    conteudo = file.read()
    contentJson = json.loads(conteudo)
    return contentJson

contentJson = carregarDados()


def mediaSalarios(contentJson):
    soma = 0.0
    for item in contentJson:
        soma = soma + item['salario']

    util.media = soma / len(item)
    return media

def mediaIdades(contentJson):
    somma = 0.0
    for idades in contentJson:
        somma = somma + idades['idade']

    util.mediaId = somma / len(idades)
    return mediaId