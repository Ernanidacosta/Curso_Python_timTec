import unittest

from dominio import Proposicao

class ProposicaoTest(unittest.TestCase):
        
    def test_protecao_atributos(self):
        proposicao = Proposicao('nome', 'termos ementa')
        proposicao.nome = 'novo nome'
        self.assertEqual('nome', proposicao.nome)
