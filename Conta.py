import random
import datetime

from Historico import *
from Pessoa import *

class Conta:

    """
        Classe que representa a conta:

        '''
        Atributos
        ---------
        titular:str
            referente a conta que tem um titular
        numero:int
            referente ao numero da conta do titular
        saldo:float
            referente ao valor que contem na conta
        historico:
            referente ao historico de movimentação na conta

        Metodos
        -------
        sacar( valor: float)
            saca o valor da conta
        depositar(valor: float)
            deposita o valor na conta
        transferir(valor: float , destiono: int)
            transfere o valor para uma conta apartir do numero da conta de destino
        extrato()
            retorna todos os dados da conta
    
    """
    slots = ['_titular','_numero','_saldo','historico']
    def __init__(self, titular, numero,senha, saldo=0.0,limite = 1000):
        self._titular = titular
        self._numero= numero
        self._saldo = saldo
        self._limite = limite
        self._senha = senha
        self._historico = Historico()
        
    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self,p):
        self._titular = p
    
    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, num):
        self._numero = num
    
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self,lim):
        self._limite = lim
    
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self,pw):
        self._senha = pw
    
    @property
    def historico(self):
        return self._historico
    @historico.setter
    def historico(self,h):
        self._historico = h
   
    def sacar(self,valor):

        """
        Retira um valo da conta solicitado pelo o usuário.
        
        Parametros
        ----------
        valor: float
            o valor é subtraido do saldo, caso o valor seja menor que o saldo.
             
        Retorno
        -------
            Retona o valor booleano verdadeiro caso seja a operação seja realizada com sucesso, caso contrario falso.
        
        Atributos:
        ---------
        valor:float
            recebe o valor que o usuario dejesa sacar e transforma em float para realizar operação. 
        
        """

        valor = float(valor)
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            self._historico.add_transacao(f'{datetime.datetime.now()} - Saque realizado com sucesso! Valor: {valor}\n')
            return True
        else:
            self._historico.add_transacao(f'{datetime.datetime.now()} - Saque não realizado!\n')
            return False

    def depositar(self,valor):

        """
        Deposita um valo da conta solicitado pelo o usuário.
        
        Parametros
        ----------
        valor: float
            o valor é adicionado do saldo, caso seja maior que 0.
        
        Retorno
        -------
            Retona o valor booleano verdadeiro caso seja a operação seja realizada com sucesso, caso contrario falso.
        
        Atributos:
        ---------
        valor:float
            recebe o valor que o usuario dejesa depositar e transforma em float para realizar operação. 
        
        """
        valor = float(valor)
        if valor >= 0:
            self.saldo+= valor
            self.historico.add_transacao(f'{datetime.datetime.now()} - Deposito realizado com sucesso! Valor: {valor}\n')
            return True
        else:
            self.historico.add_transacao(f'{datetime.datetime.now()} - Deposito não realizado!\n')
            return False

    def transferir(self,origem,destino, valor):
        """
            Tranfere um valo da conta solicitado pelo o usuário para uma conta destino.
            a conta de destino é obtida através do numero da conta. 
            
            Parametros
            ----------
            valor: float
                o valor é adicionado do saldo, caso seja maior que 0.
            
            Retorno
            -------
                Retona o valor booleano verdadeiro caso seja a operação seja realizada com sucesso, caso contrario falso
        """
        
        valor = float(valor)
        if self.numero == origem.numero:
            self.saldo -= valor 
            destino.saldo += valor
            return True
           

    
    def __str__(self) -> str:
        return f'Titular: {self._titular}\nNúmero: {self._numero}\nSaldo: {self._saldo}'

    def extrato(self):
        """
            Retorna os dados do titular da conta 
            
            Parametros
            ----------
            Não possui parametros
            
            Retornos
            -------
                Retona uma string com todos os dados do titular da conta
        """
        self._historico.add_transacao(f'Extrato realizado com sucesso\n')
        return f'{self.titular}\nNúmero: {self.numero}\nSaldo: {self.saldo}'
       
    



