import sys
import xml.etree.ElementTree as ET
import urllib.request as request


def cria_url(ano, dtInicio, dtFim):
    url = 'https://www.camara.leg.br//SitCamaraWs/Proposicoes.asmx/ListarProposicoes?sigla=PL&numero=&ano={}&datApresentacaoIni={}&datApresentacaoFim={}&parteNomeAutor=&idTipoAutor=&siglaPartidoAutor=&siglaUFAutor=&generoAutor=&codEstado=&codOrgaoEstado=&emTramitacao='
    return url.format(ano, dtInicio, dtFim)


def abre_url(url):
    req = request.urlopen(url)
    if req.getcode() == 200:
        return req.read()
    else:
        return None


def percorre(dados):
    proposicoes = ET.fromstring(dados)
    filtro = sys.argv[1]
    proposicoes_filtradas = []

    for proposicao in proposicoes:
        obj = extraiTexto(proposicao)
        if filtro in obj['txtEmenta']:
            proposicoes_filtradas.append(obj)
    
    for proposicao in proposicoes_filtradas:
        print(proposicao)


def extraiTexto(proposicao):
    attrs = ('txtEmenta', 'nome')
    prop_dict = {}
    for tag_filha in proposicao:
        if tag_filha.tag in attrs:
            prop_dict[tag_filha.tag] = tag_filha.text.strip()
    return prop_dict


ano = int(input('Digite o ano: '))
dtInicio = input('Data Inicio: ')
dtFim = input('Data Fim: ')

url = cria_url(ano, dtInicio, dtFim)
percorre(abre_url(url))