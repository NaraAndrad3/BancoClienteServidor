import datetime
import threading

from BD import *

from Conta import *
from Pessoa import *
from Historico import *

class BancoGeral:
    __slots__ = ['data']
    def __init__(self) :
        self.data = Data("localhost","Banco","root","nara1967")
    
    def add_pessoa(self,nome,cpf,nascimento):
        retorno = self.data.Buscar(cpf)
        if retorno == False:
            self.data.cadastrarPessoa(nome,cpf,nascimento)
            print('Pessoa inserida no banco')
            return True
        else:
            return False
    
    def buscarPessoa(self,cpf):
        retorno = self.data.Buscar(cpf)
        if retorno:
            return retorno
        else:
            return False
    
    def verificaSenha(self,cpf,senha):
        print('ate aqui pt. 3')
        retorno = self.data.verifcaSenha(senha)
        if retorno:
            return retorno
        else:
            return False

    def add_conta(self,cpf,senha,numero):
        retorno = self.data.BuscarConta(numero)
        id = self.data.pegaId(cpf)
        print(id)
        print(retorno)
        if retorno == False:
            if id:  
                id = int(id)
                saldo = 0.0
                limite = 1000
                saldo = float(saldo)
                limite = float(limite)
                ret = self.data.AdicionarConta(numero,saldo,limite,senha,id)
                print('Conta cadastrada')
                if ret:
                    return True
                else:
                    print('Não foi cadastrado')
            else:
                return False      
        else:
            print('Conta já cadastrada')
    
    def pegaConta(self,cpf): 
        id = self.data.pegaId(cpf)
        retorno = self.data.pegaConta(id)
        if retorno:
            titular = str(retorno[5])
            numero = retorno[1]
            senha = retorno[4]
            saldo = retorno[2] 
            limite = retorno[3]
            conta = Conta(titular,numero,senha,saldo,limite)
            return conta
        else:
            return False
    def mostrarHistorico(self,cpf):
        id = self.data.pegaId(cpf)
        retorno = self.data.mostraHistorico(id) #lista de tuplas
        if retorno:
            resultado = ""
            for i in retorno:
                resultado += "-------------------------------------------------------------------\nTipo de Transação : {}\nValor: R$ {}\nRealizado em: {}\n-------------------------------------------------------------------\n".format(i[1], i[2], i[3])
            return resultado
        else:
            return False    
    
    def depositar(self,cpf,conta,valor):
            id = self.data.pegaId(cpf)
            conta.saldo += valor
            dataT = datetime.datetime.now()
            retorno = self.data.atualizaSaldo(conta.saldo,id)
            if (retorno == True):
                retorno = self.data.historico('Deposito',valor,dataT,id)
                if retorno == True:
                    return True
                else:
                    return False
            else:
                    return False
                    
    def retornaId(self,cpf):
        return self.data.pegaId(cpf)

    def sacar(self,cpf,conta,valor):
        id = self.data.pegaId(cpf)
        valor = float(valor)
        conta.saldo -= valor
        dataT = datetime.datetime.now()
        retorno = self.data.atualizaSaldo(conta.saldo,id)
        if (retorno == True):
            ret = self.data.historico('Saque',valor,dataT,id)
            if (ret == True):
                return True
            else:
                return False
        else:
                return False

    #origem: ojeto class conta
    #destino: numero da conta
    #valor a ser transferido
    #cpf : cpf da conta origem

    def buscaConta(self,numero):
        return self.data.BuscarConta(numero)  

    def transferencia(self,cpf,origem,destino,valor):
        id = self.data.pegaId(cpf)
        retorno = self.data.BuscarConta(destino)
        idClienteId = retorno[5]
        cpfDestino = self.data.pegaCpf(idClienteId)
        idDestino = self.data.pegaId(cpfDestino)
        nomeOrigem = self.data.retornaNome(cpf)
        nomeDestino = self.data.retornaNome(cpfDestino)
        #pega o cpf a partir do Conta.Cliente_idCliente do destino
        destino = self.pegaConta(cpfDestino)
        if valor > 0:
            if origem.saldo > 0 and origem.saldo >= valor:
                if destino:
                    dataT = datetime.datetime.now()
                    origem.saldo -= valor
                    self.data.historico(f'Trasferencia efetuada para {nomeDestino[0]}',valor,dataT,id)
                    destino.saldo += valor
                    self.data.historico(f'Trsferencia recebida de {nomeOrigem[0]}',valor,dataT,idClienteId)
                    atualizaOrigem = self.data.atualizaSaldo(origem.saldo,id)
                    atualizaDestino = self.data.atualizaSaldo(destino.saldo,idDestino)
                    if(atualizaOrigem == True and atualizaDestino == True):
                        return True
                    else:
                        return False
                return True
            else:
                return False
  




        


    

           
            
    
   

    
    