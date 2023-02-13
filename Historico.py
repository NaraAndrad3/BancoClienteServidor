import datetime

class Historico():
    __slots__ = ['data_criacao','transacoes']
    def __init__(self):
        self.data_criacao = datetime.datetime.now()
        self.transacoes = []

    def add_transacao(self, t):
        self.transacoes.append(t)

    def imprimir_transacoes(self): 
        hist = 'Conta Criada em :'
        hist =hist + str(self.data_criacao)
        for t in self.transacoes:
            hist += t
        return hist

