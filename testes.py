import unittest

from classes import Produto, Funcionario

class TestProduto(unittest.TestCase):
    def test_criacao_produto(self):
        produto = Produto(1, "Bosch", "Filtro de óleo", 20, 50.00)
        self.assertEqual(produto.idProduto, 1)
        self.assertEqual(produto.marca, "Bosch")
        self.assertEqual(produto.tipo, "Filtro de óleo")
        self.assertEqual(produto.quantidade, 20)
        self.assertEqual(produto.valor, 50.00)

    def test_calculo_valor_total(self):
        produto = Produto(102, "NGK", "Velas de ignição", 4, 35.00)
        self.assertEqual(produto.calcular_valor_total(), 140.00)

    def test_quantidade_insuficiente(self):
        produto = Produto(103, "Valeo", "Pastilha de freio", 5, 120.00)
        self.assertEqual(produto.assertFalse(produto.tem_estoque()))

class TestFuncionario(unittest.TestCase):
    def test_criacao_funcionario(self):
        funcionario = Funcionario(1, "Carlos Santos", "12345678900", "carlos_santos@autocenterfernandes.com", "999999999",
                                  "Rua A, 123", "Mecânico", "Oficina", 3500.00, False)
        self.assertEqual(funcionario.idFuncionario, 1)
        self.assertEqual(funcionario.nome, "Carlos Santos")
        self.assertEqual(funcionario.cpf, "12345678900")
        self.assertEqual(funcionario.email, "carlos_santos@autocenterfernandes.com")
        self.assertEqual(funcionario.contato, "999999999")
        self.assertEqual(funcionario.endereco, "Rua A, 123")
        self.assertEqual(funcionario.cargo, "Mecânico")
        self.assertEqual(funcionario.departamento, "Oficina")
        self.assertEqual(funcionario.salario, 3500.00)
        self.assertFalse(funcionario.admin)



if __name__ == "__main__":
    unittest.main()