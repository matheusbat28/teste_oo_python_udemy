from cliente import Cliente
from contacorret import ContasCorrente
from contaPoup import ContaPoupanca

class Banco:
    def __init__(self):
        self._clientes = []
        self._contas = []

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


    def criardict(self, chave, valor):
        return  dict(zip(chave, valor)).items()

    def deposito(self, nome, valor):
        contas = self.puxarContaCliente(nome)
        contas.depositar(valor)
        return print(f'deposito de R$:{valor:.2f} com sucesso')

    def sacar(self, nome, valor):
        contas = self.puxarContaCliente(nome)
        contas.sacar(valor)
        return print(f'saque de R$:{valor} com sucesso')


    def limiteCC(self, nome, valor):
        contas = self.puxarContaCliente(nome)
        if type(contas) == ContasCorrente:
            contas.mudarlimite(valor)
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
        cont = 0
        for i in self.clientes:
            if i.nome != nome:      
                cont += 1  
            elif i.nome == nome:
                conta = self.contas[cont] 
                return conta 
                 
    def checarConta(self, nome):
        for i in self.contas:
            if self.puxarContaCliente(nome) in self.contas:
                print(f'é desse banco ')
                break
            else:
                print(f'não é desse banco')
                break

    
    def relatorio(self, nome):
        contas = self.puxarContaCliente(nome)
        for i in self.clientes:
            index = self.clientes.index(i)
        
        print(f'Cliente\n nome: {self.clientes[index].nome}\n idade: {self.clientes[index].idade}')
        if type(contas) == ContasCorrente:
            print(f'Conta\n agencia: {self.contas[index].agenica}\n numero: {self.contas[index].numero}\n saldo: {self.contas[index].saldo}\n limite: {self.contas[index].limite}')
        else:
             print(f'Conta\n agencia: {self.contas[index].agenica}\n numero: {self.contas[index].numero}\n saldo: {self.contas[index].saldo}')
 
