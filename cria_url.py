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
ano = int(input('Digite o ano: '))
dtInicio = int(input('Data Inicio: '))
dtFim = int(input('Data Fim: '))

url = cria_url(ano, dtInicio, dtFim)
print(abre_url(url))
