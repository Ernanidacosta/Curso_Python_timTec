import buscador_de_pls

with open('retorno.xml', 'wb') as data:
    response = abre_url(cria_url(2011, '14/11/2011', '16/11/2011'))
    data.write(response)
with open('retorno.xml', 'rt', encoding='utf-8') as data:
    percorre(data.read())