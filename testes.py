import unittest

from classes import Produto

class TestProduto(unittest.TestCase):
    def test_criacao_produto(self):
        produto = Produto(1, "Bosch", "Filtro de óleo", 20, 50.00)
        self.assertEqual(produto.idProduto, 1)
        self.assertEqual(produto.marca, "Bosch")
        self.assertEqual(produto.tipo, "Filtro de óleo")
        self.assertEqual(produto.quantidade, 20)
        self.assertEqual(produto.valor, 50.00)