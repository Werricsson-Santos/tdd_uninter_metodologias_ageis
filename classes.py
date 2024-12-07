class Produto:
    def __init__(self, idProduto, marca, tipo, quantidade, valor):
        self.idProduto = idProduto
        self.marca = marca
        self.tipo = tipo
        self.quantidade = quantidade
        self.valor = valor
    
class Funcionario:
    def __init__(self, idFuncionario, nome, cpf, email, contato, endereco, cargo, departamento, salario, admin):
        self.idFuncionario = idFuncionario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.contato = contato
        self.endereco = endereco
        self.cargo = cargo
        self.departamento = departamento
        self.salario = salario
        self.admin = admin