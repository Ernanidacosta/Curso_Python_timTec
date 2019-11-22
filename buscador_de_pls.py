import xml.etree.ElementTree as ET
import urllib.request as request

def cria_url(ano, dtInicio, dtFim):
    url = 'https://www.camara.leg.br//SitCamaraWs/Proposicoes.asmx/ListarProposicoes?sigla=PL&numero=&ano={}&dataApresentacaoIni={}&dataApresentacaoFim={}&parteNomeAutor=&idTipoAutor=&siglaPartidoAutor=&siglaUFAutor=&generoAutor=&codEstado=&codOrgaoEstado=&emTramitacao='
    return url.format(ano, dtInicio, dtFim)

def abre_url(url):
    req = request.urlopen(url)
    if req.getcode() == 200:
        return req.read()
    else:
        return None

def percorre(dados):
    proposicoes = ET.fromstring(dados)
    for proposicao in proposicoes:
        print(proposicao)


ano = int(input('Digite o ano: '))
dtInicio = input('Data Inicio: ')
dtFim = input('Data Fim: ')

url = cria_url(ano, dtInicio, dtFim)
percorre(abre_url(url))
