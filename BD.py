import mysql.connector

class Data:
    def __init__(self,host,db,user,password):
        self.conexao = mysql.connector.connect(host = host,db=db,user=user,password=password)
        self.cursor = self.conexao.cursor()
    
    #cadastra uma pessoa no banco
    def cadastrarPessoa(self,nome,cpf,nascimento):
        datas = (nome,cpf,nascimento)
        sql = "INSERT INTO Cliente(nome,cpf,nascimento) VALUES(%s,%s,%s);"
        self.cursor.execute(sql,datas)
        print('Cadastrou a pessoa')

        self.conexao.commit()
    
    #Adiciona as contas ao banco
    def AdicionarConta(self,numero,saldo,limite,senha,id):
        numero =str(numero)
        datas = (numero,saldo,limite,senha,id)
        sql = "INSERT INTO Conta(numero,saldo,limite,senha,Cliente_idCliente) VALUES(%s,%s,%s,MD5(%s),%s);"
        self.cursor.execute(sql,datas)
        self.conexao.commit()
        return True
    #pega o id de um cliente no banco a partir da cpf
    def pegaId(self,cpf):
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
        print('ate aqui foi 1')
        sql = f"SELECT cpf FROM Cliente WHERE idCliente = {idClienteId};"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        self.conexao.commit()
        print('ate aqui foi 2')
        if retorno:
            return retorno[0]
        else:
            return False
    
    def retornaNome(self,cpf):
        sql = f"SELECT Nome FROM Cliente WHERE Cpf = {(cpf)}"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        if retorno:
            return retorno
        else:
            return False


    #Busca um cliente no banco a partir do cpf
    def Buscar(self,cpf):
        sql = f"SELECT * FROM Cliente WHERE cpf = {(cpf)};"
        self.cursor.execute(sql)
        retorno = self.cursor.fetchone()
        if retorno != None:
            return retorno
        else:
            return False
    #Busca um conta no banco a partir do numero
    def BuscarConta(self,numero):
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
        sql = f"SELECT * FROM Conta WHERE Senha = MD5({(senha)});"
        self.cursor.execute(sql)
        print('até aqui foi pt. 1')
        retorno = self.cursor.fetchone()
        self.conexao.commit()
        if retorno:
            return retorno
        else:
            return False

    #Pega uma conta no banco com base no id do cliente
    def pegaConta(self,id):
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
    
    #Para adicionar o historico à classe tabela
    def historico(self,tipoTransacao,valor,data,conta_idConta):
        try:
            var = (tipoTransacao,valor,data,conta_idConta)
            sql = "INSERT INTO Historico(TipoTransação,Valor,Data,Conta_idConta) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(sql,var)
            self.conexao.commit()
            return True
        except:
            return False
    
    def mostraHistorico(self, id):
        sql = f"SELECT * FROM Historico WHERE Conta_idConta = {(id)} "
        self.cursor.execute(sql)
        retorno = self.cursor.fetchall()
        if retorno:
            return retorno
        else:
            return False
            


        
        



    
    

    
