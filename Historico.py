import datetime

class Historico():
    """
        Classe que representa a Historico:

        '''
        Atributos
        ---------
        data_criacao: Datetime
            Contém a hora e data de uma transação realizada
        transacao: list
            Contem uma lista de transações realizadas e  data e hora.


        Metodos
        -------
        add_transacao(t:object)
    
    """
    __slots__ = ['data_criacao','transacoes']
    def __init__(self):
        self.data_criacao = datetime.datetime.now()
        self.transacoes = []

    def add_transacao(self, t):
        """
            Função que adiciona um mensagem na lista de transações
            Esta mensagem contem informações acerca das transações realizadas pelo cliente

            Parametros
            ----------
            t: str
                mensagem que contem as informações  de transações
        """

        self.transacoes.append(t)

    def imprimir_transacoes(self):
        """
            Função que retorna  todas as transações realizadas pelo cliente 

            Parametros
            ----------
            
            Retornos
            ----------
                retorna a lista de transações realizadas
                
        """
        hist = 'Conta Criada em :'
        hist =hist + str(self.data_criacao)
        for t in self.transacoes:
            hist += t
        return hist

