from contas import  Contas

class ContasCorrente(Contas):
    def __init__(self):
        super().__init__()
        self._limite = 300

    @property
    def limite(self):
        return self._limite

    def mudarlimite(self, novoLimite):
        self._limite += novoLimite
        return print('limite alterado com sucesso')

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            if self.saldo >= valor:
               self.saldo -= valor
            else:
                self.saldo -= valor
                self._limite = self.limite + (self.saldo)
                self.saldo = 0
            return print('saque comcluido')
        else:
            return print(f'esse valor {valor} não pode ser sacado')
                
    
