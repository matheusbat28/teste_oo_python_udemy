from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
