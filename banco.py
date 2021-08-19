import funcao
from cliente import Cliente
from contacorret import ContasCorrente
from contaPoup import ContaPoupanca

class Banco:
    def __init__(self):
        self._agencia = "111"
        self._clientes = []
        self._contas = []

    @property
    def agenica(self):
        return self._agencia

    @property
    def clientes(self):
        return self._clientes  

    @property
    def contas(self):
        return self._contas 

    def criarCliente(self, nome, idade):
        Cliente(nome, idade)

    def criarConta(self, tipo):
        if tipo == "1":
            ContaPoupanca()
        elif tipo == "2":
            ContasCorrente()

    def criarUsuarios(self, nome, idade, tipo):
        self.clientes.append(self.criarCliente(nome, idade))
        self.contas.append(self.criarConta(tipo))


    def __str__(self):
        return print(self.clientes)