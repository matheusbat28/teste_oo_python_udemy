import funcao
from abc import abstractmethod

class Contas:
    def __init__(self):
        self._agencia = "111"
        self._numero = funcao.gerarNumero()
        self._saldo = 0

    @property
    def agenica(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novoSaldo):
        self._saldo = novoSaldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self):
        pass

    @abstractmethod
    def tansferir(self):
        pass