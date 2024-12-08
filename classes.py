#Após a criação dos testes, criamos as classes ou features a fim de atingir o objetivo de passar em todos os testes.

#Implementação da classe Produto
class Produto:
    def __init__(self, idProduto, marca, tipo, quantidade, valor):
        self.idProduto = idProduto
        self.marca = marca
        self.tipo = tipo
        self.quantidade = quantidade
        self.valor = valor

    def exibir_informacoes(self):
        print("\n")
        print("Tipo: ", self.tipo)
        print("Marca: ", self.marca)
        print("Quantidade: ", self.quantidade)
        print("Valor: ", self.valor)
        print("\n")
    
    #Calcula o valor total de acordo com a quantidade
    def calcular_valor_total(self):
        return self.quantidade * self.valor

    #Verifica se há quantidade suficiente no estoque a partir da solicitação do cliente.
    def tem_estoque(self, quantidade_requerida):
        return self.quantidade >= quantidade_requerida
    
#Implementação da classe funcionário
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

    def exibir_informacoes(self):
        print("\n")
        print("Nome: ", self.nome)
        print("Cargo: ", self.cargo)
        print("Email: ", self.email)
        print("Contato: ", self.contato)
        print("Endereço: ", self.endereco)
        print("\n")

    #Simula acesso a area administrativa
    def acessar_area_admin(self):
        #O acesso só é liberado se o funcionário for admin.
        response = "Acesso liberado." if self.admin else "Você não possui acesso administrativo."

        return response