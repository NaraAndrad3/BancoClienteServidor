import random
import datetime

from Historico import *
from Pessoa import *

class Conta:
    slots = ['_titular','_numero','_saldo','historico']
    #manda o obj de pessoa pra ca
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
        valor = float(valor)
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            self._historico.add_transacao(f'{datetime.datetime.now()} - Saque realizado com sucesso! Valor: {valor}\n')
            return True
        else:
            self._historico.add_transacao(f'{datetime.datetime.now()} - Saque não realizado!\n')
            return False

    def depositar(self,valor):
        valor = float(valor)
        if valor >= 0:
            self.saldo+= valor
            self.historico.add_transacao(f'{datetime.datetime.now()} - Deposito realizado com sucesso! Valor: {valor}\n')
            return True
        else:
            self.historico.add_transacao(f'{datetime.datetime.now()} - Deposito não realizado!\n')
            return False

    def transferir(self,origem,destino, valor):
        valor = float(valor)
        if self.numero == origem.numero:
            self.saldo -= valor 
            #self._historico.add_transacao(f'{datetime.datetime.now()} - Transferência realizada para {destino.titular.nome} Valor: {valor}\n')
            destino.saldo += valor
            #destino.historico.add_transacao(f'{datetime.datetime.now()} - Transferência recebida de {origem.titular.nome}  Valor: {valor}\n')
            return True
           

    
    def __str__(self) -> str:
        return f'Titular: {self._titular}\nNúmero: {self._numero}\nSaldo: {self._saldo}'

    def extrato(self):
        self._historico.add_transacao(f'Extrato realizado com sucesso\n')
        return f'{self.titular}\nNúmero: {self.numero}\nSaldo: {self.saldo}'
       
    



'''''pessoa = Pessoa('nara','Dias','123','1234')
conta = Conta(pessoa,133)

print(conta.adicionarConta(conta))

conta.depositar(100)
conta.extrato()
'''''



