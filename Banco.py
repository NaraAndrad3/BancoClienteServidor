import datetime
import threading

from BD import *

from Conta import *
from Pessoa import *
from Historico import *

class BancoGeral:
    """
    Classe que representa a instituição bancária

    ...

    Attributos
    ----------
    data: Objeto
        Instância da classe Data
    
    Métodos
    -------
    
    add_pessoa(nome,cpf,nascimento): 
        Realiza o cadastro de um cliente no Banco
    buscarPessoa(cpf):
        Faz a busca de um cliente no sistema a partir do atributo cpf
    verificaSenha(cpf,senha):
        faz a verificação da autenticidade da senha utilizada por um cliente
    add_conta(cpf,senha,numero):
        Adiciona uma conta e vincula a um cliente já cadastrado no sistema
    pegaConta(cpf):
        Seleciona os dados de uma cliente do sistema e retorna um objeto da classe conta
    mostrarHistorico(cpf):
        Imprime o histórico de uma conta
    depositar(cpf,conta,valor):
        Realiza a operação de depósito em uma conta
    sacar(cpf,conta,valor):
        Realiza a operação de saque em uma conta
    transferencia(cpf,origem,destino,valor):
        realiza a operação de transfêrencia entre duas contas
    """

    __slots__ = ['data']
    def __init__(self) :
        """
        Método construtor com os atibutos necessários à classe BancoGeral.

        Retorno:
        -------
            None.

        """
        self.data = Data("localhost","Banco","root","nara1967")
    
    def add_pessoa(self,nome,cpf,nascimento):
        """
        Método para cadastrar uma pessoa no sistema

        Parâmetros:
        ----------

        nome: str, obrigatório.
            Nome completo do cliente a ser cadastrado.
        cpf: Str, obrigatório.
            Cpf da pessoa a ser cadastrada
        nascimento: Str, Obrigatório.
            Data de nascimento da pessoa a ser cadastrada
        
        Atributos:
        ----------
        retorno: tupla ou boolean.
            recebe o retorno do método buscar, se o retorno não existir(False) o cliente é cadastrado.
        
        Retorno:
        -------
            Retorna True se a pessoa for cadastrada ou False se a pessoa já estiver cadastrada no sistema. 

        """
        retorno = self.data.Buscar(cpf)
        if retorno == False:
            self.data.cadastrarPessoa(nome,cpf,nascimento)
            return True
        else:
            return False
    
    def buscarPessoa(self,cpf):
        """
        Método para realizar a busca por um cliente no sistema bancário.

        Parâmetros:
        ----------
        cpf: str, obrigatório.
            Cpf do cliente a ser buscado no sistema 
        
        Atributos:
        ---------
        retorno: tupla ou boolean.
            Atributo que recebe o que é retornado do método Buscar
        
        Retorno: tupla ou boolean.
            retorna o que o atributo retorno recebe, se receber uma tupla, ela é retornada, se receber False 
            o retorno do método é False.

        """
        retorno = self.data.Buscar(cpf)
        if retorno:
            return retorno
        else:
            return False
    
    def verificaSenha(self,senha):
        """
        Método para verificar a autenticidade da senha utilizada por um cliente.

        Parâmetros:
        ----------
        senha: str, obrigatório.
            variável  que armazena a senha digitada pelo cliente.
        
        Atributos:
        ----------
        retorno: str ou tupla.
            Atributo que recebe o retorno do método verificaSenha
        
        Retorno:
        --------
        retorno: tupla.
            Caso seja retornada uma tupla e armazenada no atributo retorno.
        False: boolean.
            Caso seja retornado um valor boleano para o atributo retorno

        """
        retorno = self.data.verifcaSenha(senha)
        if retorno:
            return retorno
        else:
            return False

    def add_conta(self,cpf,senha,numero):
        """
        Método para vincular uma conta a uma pessoa já cadastrada no sistema

        Parãmetros:
        ----------
        cpf: str, obrigatório.
            cpf da pessoa a qual a conta será vinculada
        senha: str, obrigatória.
            senha definida pelo cliente no ato do cadastro
        numero: int, obrigatório.
            Número definido (aleatóriamente) para a conta.
        
        Atributos:
        ----------
        retorno: tupla ou boolean.
            Atributo que armazena o retorno do método BuscarConta
        id: int
            Atributo que recebe o retorno do método pegaId.
        
        Retorno:
        -------
            Retorna True caso a peração seja realizada e False caso não seja realizada.
        """
        retorno = self.data.BuscarConta(numero)
        id = self.data.pegaId(cpf)
        if retorno == False:
            if id:  
                id = int(id)
                saldo = 0.0
                limite = 1000
                saldo = float(saldo)
                limite = float(limite)
                ret = self.data.AdicionarConta(numero,saldo,limite,senha,id)
                if ret:
                    return True
                else:
                    print('Não foi cadastrado')
            else:
                return False      
        else:
            print('Conta já cadastrada')
    
    def pegaConta(self,cpf):
        """
        Método que acessa o banco de dados e recupera os dados da conta de um cliente especifico.

        Parâmetros:
        ----------
        cpf: Str, obrigatório.
            Cpf da pessoa que terá os dados buscados
        
        Atributos:
        ----------
        id: int
            Atributo que recebe o retorno do método pegaId.
        retoorno: tupla ou boolen
            Atributo que recebe o retorno do método pegaConta
        
        Retorno:
        --------
            Retorno o objeto conta se existir, ou retornar False se não existir
        """
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
        """
        Método para formatar o histórico a ser exibido para o cliente

        Parâmetros:
        -----------
        cpf: str, obrigatório.
            Cpf do cliente titular da conta
        
        Atributos:
        ---------
        id: int
            Atributo que recebe o retorno do método pegaId.
        retorno: tupla ou boolean
            Atributo que recebe o retorno do método mostraHistorico
        
        Retorno:
        -------
            Retorna uma string, caso o resultado do atributo retorno exista, ou retorna False caso ele não exista
        """
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
            """
            Método que realiza a operação de depósito em uma conta

            Parâmetros:
            ----------
            cpf: str, obrigatório.
                Cpf do titular da conta em que será realizado o depósito
            conta: Objeto, obrigatório.
                Objeto da classe conta referente aos dados do cliente titular
            valor: float, obrigatório.
                Valor a ser depositado na conta
            
            Atributos:
            ---------
            id: int
                Armazena o retorno do método pegaId.
            retorno: boolean.
                Armazena o retorno do método atualizaSaldo.
            dataT: date
                Atributo que armazena a data e horário da operação

            Retorno:
            -------
                Retorna True se a operação for bem sucedida, caso contrário retorna False
            """
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
                    
    def sacar(self,cpf,conta,valor):
        """
        Método para realizar a operação de saque em uma conta.

        Parâmetros:
        ----------
        cpf: Str, obrigatório.
            Cpf do cliente titular da conta em que a operação será realizada
        conta: Objeto, obrigatório
            Objeto da classe conta referente aos dados do cliente titular
        valor: Float, obrigatório
            Valor a ser sacado da conta
        
        Atributos:
        id: int
            Atributo que recebe o retorno do método pegaId
        dataT: date
            Atributo que armazena a data e horário da operação

        Retorno:
        -------
            Retorna True se a operação for bem sucedida, caso contrário retorna false
        """
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


    def transferencia(self,cpf,origem,destino,valor):
        """
        Método que realiza a operação de transferencia entre duas contas

        Parâmetros:
        ----------
        cpf: str, obrigatório
            Cpf do cliente titulat da conta de origem
        origem: Objeto. obrigatório.
            Objeto da classe conta referente aos dados do cliente titular
        destino: str, obrigatório.
            Numero da conta de destino
        valor: float, Obrigatório.
            Valor a ser trsnaferido entre as contas
        
        Atributos:
        ---------
        id: int
            Atributo que armazena o retorno do método pegaId
        retorno: tupla ou boolean
            Atributo que armazena  o retorno do método BuscarConta, que pode ser uma tupla ou um valor booleano
        idClienteId: int
            Atributo que armazena a posição 5 do atributo retorno(caso exista)
        cpfDestino: Str
            Atributo que armazena o retorno do método pegaCpf
        idDestino: int
             Atributo que armazena o retorno do método pegaId
        nomeDestino: Str
            Atributo que aramzena o nome do titular da conta de destino

        Retorno:
        ------- 
            Retorno um valor booleano(True ou False), True se a operação for concluida, caso contrário retorna False
        """
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
  




        


    

           
            
    
   

    
    