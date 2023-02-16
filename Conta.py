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
   
    
    def __str__(self) -> str:
        return f'Titular: {self._titular}\nNúmero: {self._numero}\nSaldo: {self._saldo}'



