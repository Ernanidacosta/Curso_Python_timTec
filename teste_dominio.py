import unittest

from dominio import Proposicao

class ProposicaoTest(unittest.TestCase):
    def setUp(self):
        self.proposicao = Proposicao('nome', 'termos ementa')

    def test_protecao_atributos(self):
        self.proposicao.nome = 'novo nome'
        self.assertEqual('nome', self.proposicao.nome)

    def test_menciona_termo(self):
        self.assertTrue(self.proposicao.menciona_termo('ementa')) 