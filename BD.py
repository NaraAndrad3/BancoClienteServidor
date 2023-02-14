import mysql.connector

class Data:

    """
        Classe que representa a Data:

        '''
        Atributos
        ---------
        host: str
            ip da conexão com banco de dados.
        bd:str
            nome do banco de dados que pertence ao projeto.
        user: str
            nome do usuario do banco de dados.
        password:str
            senha do banco de dados para permitir a conexão.

               
        Metodos
        -------
        cadastrarPessoa(nome: str, cpf:str, nascimento: str )
            recebe os dados passados por parametros e realiza a operação sql de inserção dos dados na tabela cliente do banco dedos.
        AdicionaConta(numero: int, saldo:float, limite:float, senha:str, id: int)
            cadastrar a conta da pessoa com os paramentros da conta  e o id referente a pessoa ja cadastrada.
        pegaId(cpf:str)
            busca o id do usuario por meior do cpf.
        pegaCpf(idCliente: int)
            busca o cpf do cliente por meior do id.
        retornaNome(cpf:str)
            busca o nome do cliente pelo cpf.
        Buscar(cpf:str)
            busca todos os dados do cliente pelo cpf.
        BuscarConta(numero: int)
            buscar a conta do cliente pelo numeo da conta.
        AtualizaSaldo(newSaldo: float, id: int)
            Atualiza o saldo da conta pelo id e recebendo novo saldo.
        historico(TipoTransacao: str,valor: float,data: dateTime,conta_idConta: int)
            Insere o histórico de transação
        MostraHistorico(id:int)
            retorna o de uma determinada conta pelo id
    """ 
    def __init__(self,host,db,user,password):
        self.conexao = mysql.connector.connect(host = host,db=db,user=user,password=password)
        self.cursor = self.conexao.cursor()
    
    #cadastra uma pessoa no banco
    def cadastrarPessoa(self,nome,cpf,nascimento):
        """
            Função que cadastra pessoa no banco realizando operação de inserção na tabela Cliente
            
            Parametros
            ----------
            nome:str
                nome da pessoa a ser cadastrada
            cpf:str
                cpf da pessoa
            nascimento: DATE
                Data de nascimento da pessoa
                
            Retorno
            -------
                True quando a operação é realizada com sucesso
        """
        datas = (nome,cpf,nascimento)
        sql = "INSERT INTO Cliente(nome,cpf,nascimento) VALUES(%s,%s,%s);"
        self.cursor.execute(sql,datas)
        print('Cadastrou a pessoa')

        self.conexao.commit()
        return True
    
    #Adiciona as contas ao banco
    def AdicionarConta(self,numero,saldo,limite,senha,id):
        """
            Função que cadastra conta no banco realizando operação de inserção na tabela conta passando referenciando a tabela pessoa pelo id
            
            Parametros
            ----------
            numero:int
                numero da conta
            saldo:float
                saldo da conta
            limite: float
                limite do quando pode ser inserido na conta
            senha: str
                senha da conta do cliente
            id: int
                id que pertence a pessoa cadastrada na tabela Pessoa, usado para relação entre as tabelas Pessoa e Conta
            Retorno
            -------
                True quando a operação é realizada com sucesso
        """
        numero =str(numero)
        datas = (numero,saldo,limite,senha,id)
        sql = "INSERT INTO Conta(numero,saldo,limite,senha,Cliente_idCliente) VALUES(%s,%s,%s,MD5(%s),%s);"
        self.cursor.execute(sql,datas)
        self.conexao.commit()
        return True
    #pega o id de um cliente no banco a partir da cpf
    def pegaId(self,cpf):
        """
            Funcao que realiza uma busca na tabela cliente e pega o id do cliente pelo cpf

            Parametros
            ----------
            cpf: str
                usado para realizar a busca do id onde cpf é iguai ao informado.
            Retorno
            -------
                retorna o id caso encontrado
                retorna boolean false caso o id não seja encontrado na base dados
        """
        sql = f"SELECT idCliente FROM Cliente WHERE cpf = {(cpf)};"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        self.conexao.commit()
        #print(retorno[0])
        if retorno:
            return retorno[0]    
        else:
            False
    #Pega o cpf de um cliente no banco a partir do id        
    def pegaCpf(self,idClienteId):
        """
            Funcao que realiza uma busca na tabela cliente e pega o cpf do cliente pelo id

            Parametros
            ----------
            idClienteId: int
                usado para realizar a busca do cpf onde id é iguai ao informado.
            Retorno
            -------
                retorna o cpf caso encontrado
                retorna boolean false caso o cpf não seja encontrado na base dados
        """
        sql = f"SELECT cpf FROM Cliente WHERE idCliente = {idClienteId};"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        self.conexao.commit()
        if retorno:
            return retorno[0]
        else:
            return False
    
    def retornaNome(self,cpf):
        """
            Função que realiza uma busca na tabela cliente e pega o nome do cliente pelo cpf

            Parametros
            ----------
            cpf: str
                usado para realizar a busca do nome onde cpf é iguai ao informado.
            Retorno
            -------
                retorna o nome caso encontrado
                retorna boolean false caso o id não seja encontrado na base dados
        """
        sql = f"SELECT Nome FROM Cliente WHERE Cpf = {(cpf)}"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        if retorno:
            return retorno
        else:
            return False


    #Busca um cliente no banco a partir do cpf
    def Buscar(self,cpf):
        """
            Função que realiza uma busca na tabela cliente e pega todos os dados do cliente pelo cpf.

            Parametros
            ----------
            cpf: str
                usado para realizar a busca dos dados onde cpf é iguai ao informado.
            Retorno
            -------
                retorna os dados do cliente caso encontrado.
                retorna boolean false caso o id não seja encontrado na base dados.
        """
        sql = f"SELECT * FROM Cliente WHERE cpf = {(cpf)};"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        if retorno != None:
            return retorno
        else:
            return False
    #Busca um conta no banco a partir do numero
    def BuscarConta(self,numero):
        """
            Função que realiza uma busca na tabela conta e pega os dados da conta  pelo numero informado.

            Parametros
            ----------
            numero: int
                usado para realizar a busca dos dados da conta.
            Retorno
            -------
                retorna os dados caso encontrado.
                retorna boolean false caso o id não seja encontrado na base dados.
        """
        sql = f"SELECT * FROM Conta WHERE numero = {(numero)};"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        print('Retorno da conta',retorno)
        if retorno:
            return retorno
        else:
            return False

    #verifica se a senha é a correta com base no id
    def verifcaSenha(self,senha):
        """
            Função que realiza uma busca na tabela Conta e verifica se a senha esta correta, a busca é feita pelo id

            Parametros
            ----------
            id: int
                usado para realizar a busca dos dados da conta.
            Retorno
            -------
                retorna os dados caso encontrado.
                retorna boolean false caso o id não seja encontrado na base dados.
        """
        sql = f"SELECT * FROM Conta WHERE Senha = MD5({(senha)});"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        self.conexao.commit()
        if retorno:
            return retorno
        else:
            return False

    #Pega uma conta no banco com base no id do cliente
    def pegaConta(self,id):
        """
            Função que realiza uma busca na tabela conta e pega os dados da conta  pelo id informado.

            Parametros
            ----------
            numero: int
                usado para realizar a busca dos dados da conta.
            Retorno
            -------
                retorna os dados caso encontrado.
                retorna boolean false caso o id não seja encontrado na base dados.
        """
        sql = f"SELECT * FROM Conta WHERE Cliente_idCliente = {(id)}"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        self.conexao.commit()
        if retorno:
            return retorno
        else:
            return False

    #Arualiza o saldo do cliente na tabela
    def atualizaSaldo(self,newSaldo,id):
        """
            Função que realiza uma atualização na tabela conta para atualizar o saldo da conta pelo id e um novo saldo.

            Parametros
            ----------
            newSaldo: float
                usado para realizar a busca dos dados da conta.
            id: int
                id da conta que contem o saldo a ser atualizado por newSaldo
            Retorno
            -------
                retorna os dados caso encontrado.
                retorna boolean false caso o id não seja encontrado na base dados.
        """
        newSaldo = float(newSaldo)
        sql = f"UPDATE Conta SET Saldo = {(newSaldo)} WHERE Conta.Cliente_idCliente = {(id)};"
        self.cursor.execute(sql)
        cont = self.cursor.rowcount
        self.conexao.commit()
        print(cont)
        if cont > 0: #conta quantas linhas forma afetadas pelo comanod
            return True
        else:
            return False
    
    #Para adicionar o historico à classe conta
    def historico(self,tipoTransacao,valor,data,conta_idConta):
        """
            Função que realiza uma inserção do histórico na tabela histórico .

            Parametros
            ----------
            tipoTransacao: str
                string que informa o tipo de transação que será realizada.
            valor: float
                valor, o valor é usado para demontrar que ouve uma alteração na conta, exemplo,(Houve uma saque no valor de (valor))
            data: DATE
                especifica a data da transação realizada
            conta_idConta: int
                id da conta em foi realizada a operação.
            Retorno
            -------
                retorna boolena True caso a operação seja realizada com sucesso.
                retorna boolean false caso não seja realizada com sucesso..
        """
        try:
            var = (tipoTransacao,valor,data,conta_idConta)
            sql = "INSERT INTO Historico(TipoTransação,Valor,Data,Conta_idConta) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(sql,var)
            self.conexao.commit()
            return True
        except:
            return False
    
    def mostraHistorico(self, id):
        """
            Função que pega todos as transações das realizadas pelo id da conta na tabela histórico .

            Parametros
            ----------
            id: int
                id da conta que contem o saldo a ser atualizado por newSaldo
            Retorno
            -------
                retorna os dados caso encontrado.
                retorna boolean false caso o id não seja encontrado na base dados.
        """
        sql = f"SELECT * FROM Historico WHERE Conta_idConta = {(id)} "
        self.cursor.execute(sql)
        retorno = self.cursor.fetchall()
        if retorno:
            return retorno
        else:
            return False
            


        
        



    
    

    
