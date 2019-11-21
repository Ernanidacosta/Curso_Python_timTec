import unittest

from dominio import Proposicao

class TestProposicao(unittest.TestCase):
    def setUp(self):
        self.proposicao = Proposicao('nome', 'ementa de teste')

    def tearDown(self):
        print('Sempre após cada teste')

    def test_protecao_atributos(self):
        self.proposicao.nome = 'novo nome'
        self.assertEqual(self.proposicao.nome, 'nome')
    
    def test_menciona_termo(self):
        self.assertTrue(self.proposicao.menciona_termo("testes"))