from cliente import Cliente
from contacorret import ContasCorrente
from contaPoup import ContaPoupanca

class Banco:
    def __init__(self):
        self._clientes = []
        self._contas = []
        self._contaCliente = {} 

    @property
    def clientes(self):
        return self._clientes  

    @property
    def contas(self):
        return self._contas 

    @property
    def contaCliente(self):
        return self._contaCliente

    def criarCliente(self, nome, idade):
        self.clientes.append(Cliente(nome, idade))

    def criarConta(self, tipo):
        if tipo == "1":
            self.contas.append(ContaPoupanca())
        elif tipo == "2":
             self.contas.append(ContasCorrente())

    def criarUsuarios(self, nome, idade, tipo):
        self.criarCliente(nome, idade)
        self.criarConta(tipo)

    def criardict(self, dicionario ,chave, valor):
        dicionario = dict(zip(chave, valor)).items()
        return dicionario

    def deposito(self, numero, valor):
        contas = self.contas[numero]
        contas.depositar(valor)

    def sacar(self, numero, valor):
        contas = self.contas[numero]
        contas.sacar(valor)

    def limiteCC(self, numero, valor):
        contas = self.contas[numero]
        if type(contas) == ContaPoupanca:
            contas.mudarlimite = valor
            return print('limite alterado')
        else:
             return print('essa conta não tem opção de limite')

    def checarAgencia(self, conta):
        if conta.agenica() == '111':
            return print(f'a conta {conta.numero()} é desse banco')

    def checarCliente(self, nome):
        for i in self.clientes:       
            if i.nome == nome:
                print(f'{nome} é desse banco')
                break
            else:
                print(f'{nome} não é desse banco')
                break

    def puxarContaCliente(self, nome):
        for i in self.clientes:       
            if i.nome == nome:
              print(self.clientes[i])  

    def checarConta(self, numero):
        for i in self.contas:
            if i.numero == numero:
                print(f'{numero} é desse banco ')
                break
            else:
                print(f'{numero} não é desse banco')
                break


    def relatorio(self, numero):
        cliente = self.clientes[numero]
        contas = self.contas[numero]
        print(f'Cliente\n nome: {cliente.nome}\n idade: {cliente.idade}')
        if type(contas) == ContasCorrente:
            print(f'Conta\n agencia: {contas.agenica}\n numero: {contas.numero}\n saldo: {contas.saldo}\n limite: {contas.limite} ')
        else:
            print(f'Conta\n agencia: {contas.agenica}\n numero: {contas.numero}\n saldo: {contas.saldo}')
 
           