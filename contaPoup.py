from contas import Contas

class ContaPoupanca(Contas):
    def __init__(self):
        super().__init__()

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return print('saque concluido')
        else:
            return print(f'esse valor {valor} não pode ser sacado')

    