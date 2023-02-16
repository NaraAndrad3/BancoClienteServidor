import threading
import socket
from Banco import *

class ServidorTreading(threading.Thread):
    """
    Classe que representa o Servidor Multhreading
  
    Atributos:
    ----------
    socketCliente: int
        Atributo que armazena o conteido do parâmetro socketCliente
    adressCliente: int
        Atributo que armazena o conteúdo so parâmetro adressCliente
    sincThread: 
        Atributo para receber os métodos da classe lock a partir do módulo threading
    
    Métodos:
    -------
    run: 
        Método responsável por reconhecer e realizar as operações solicitadas pelo cliente
    """
    def __init__(self,adressCliente,socketCliente):
        """
        Método construtor com todos os atributos necessários para o funcionamento da classe ServidorThreading

        Parâmetros:
        ----------
        adressCliente: Str, obrigatório
            Parâmetro que armazena o endereço do cliente.
        socketCliente: int, obrigatório
            Parâmetro qe armazena a porta de conexão do cliente com o servidor
        
        Atributos:
        ----------
        socketCliente: int
            Atributo que armazena o conteido do parâmetro socketCliente
        adressCliente: int
            Atributo que armazena o conteúdo so parâmetro adressCliente
        sincThread: 
            Atributo para receber os métodos da classe lock a partir do módulo threading
    
        """
        self.socketCliente = socketCliente
        self.adressCliente = adressCliente
        self.sincThread = threading.Lock()
        threading.Thread.__init__(self)
        print('Nova conexão estabelecida',self.adressCliente)

    def run(self): #Todas as operações serão realizadas aqui
        """
        Método responsável por reconhecer e realizar as operações solicitadas pelo cliente

        Atributos:
        ---------
        banco: Objeto, obrigatório
            Instância da classe BancoGeral
        mensagem: Str
            Atributo para  armazenar a mesagem enviada pelo cliente para o servidor
        
        Retorno:
        -------
            Retorna um retorno do tipo String em qualquer situação

        
        """
        banco = BancoGeral()
        mensagem = ''
        while True:
            data = self.socketCliente.recv(1024)
            mensagem = data.decode()
            mensagem = mensagem.split('*')
            #print('mensagem recebida pelo servidor',mensagem)
            if mensagem == 's':
                break
            else:
                if mensagem[0] == '01': #operação de login
                    retornoPessoa =  banco.buscarPessoa(mensagem[1])
                    retornoConta = banco.verificaSenha(mensagem[1],mensagem[2])
                    if (retornoPessoa != False and retornoConta != False):
                            r = True
                            retornoServer = f'{r}*{retornoPessoa[1]}*{retornoConta[1]}*{retornoConta[2]}'
                            print('Retorno para o cliente: ',retornoServer)
                            self.socketCliente.send(retornoServer.encode())
                if mensagem[0] == '02': #operação de cadastro
                    r = True
                    self.sincThread.acquire() #so pode cadastrar um por vez
                    retornoPessoa = banco.buscarPessoa(mensagem[2])
                    #print('Retorno do cadastro: ',retornoPessoa)
                    if retornoPessoa == False:
                        banco.add_pessoa(mensagem[1],mensagem[2],mensagem[3])
                        banco.add_conta(mensagem[2],mensagem[4],mensagem[5]) # cpf e numero da conta
                        self.socketCliente.send('True'.encode())
                    self.sincThread.release()
                if mensagem[0] == '03': #operação de deposito
                    self.sincThread.acquire() #só pode depositar uma conta por vez
                    conta = banco.pegaConta(mensagem[1])
                    deposito = banco.depositar(mensagem[1],conta,float(mensagem[2]))
                    if deposito:
                        self.socketCliente.send('True'.encode())
                    else:
                        self.socketCliente.send('Não foi possivel realizar a operação'.encode())
                    self.sincThread.acquire()
                if mensagem[0] == '04': #Operação de saque
                    self.sincThread.acquire() # só pode sacar uma conta por vez
                    senha = banco.verificaSenha(mensagem[1],mensagem[3])
                    if senha:
                        conta = banco.pegaConta(mensagem[1])
                        saque = banco.sacar(mensagem[1],conta,float(mensagem[2]))
                        if saque:
                            self.socketCliente.send('True'.encode())
                        else:
                            self.socketCliente.send('Não foi possivel realizar a operação'.encode())
                    else:
                        self.socketCliente.send('Não foi possivel realizar a operação'.encode())
                        self.sincThread.release()
                if mensagem[0] == '05': #Operação de transferencia
                    #'{op}*{cpfAtual}*{destino}*{valor}*{senha}'
                    self.sincThread.acquire() # só pode transferir uma conta por vez
                    senha = banco.verificaSenha(mensagem[4])
                    if senha:
                        contaOrigem = banco.pegaConta(mensagem[1])
                        retorno = banco.transferencia(mensagem[1],contaOrigem,mensagem[2],float(mensagem[3]))
                        if retorno:
                            self.socketCliente.send('True'.encode())
                        else:
                            self.socketCliente.send('Não foi possivel realizar a operação'.encode())
                        self.sincThread.release()
                if mensagem[0] == '06': #Operação extrato
                    retornoPessoa = banco.buscarPessoa(mensagem[1])
                    retornoConta = banco.pegaConta(mensagem[1])
                                        #Nome               Numero                  saldo
                    extrato = f'True*{retornoPessoa[1]}*{retornoConta.numero}*{retornoConta.saldo}'
                    self.socketCliente.send(extrato.encode())
                
                if mensagem[0] == '07': #Operação de Historico
                    retornoHistorico = banco.mostrarHistorico(mensagem[1])
                    historico = f'True*{retornoHistorico}'
                    self.socketCliente.send(historico.encode())




if __name__ == '__main__':
    '''
    Main responsáve por iniciar as threadings

    Atributos:
    ---------
    Localhost: Str, Obrigatório
        Responsável por armazenar o endereço do servidor
    door: int
        Resposável por armazenar a porta de conexão com o servidor
    server:
        instância do módulo socket
    '''
    Localhost = '10.180.45.43'
    door = 9068
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((Localhost,door))
    print('Servidor iniciado')
    print('Aguardando nova conexão')
    while True:
        server.listen()
        socketCliente, adressCliente = server.accept() #aceita as conexões
        newthead = ServidorTreading(adressCliente,socketCliente) #atribui ao newThread as informação do cliente(cria obj)
        newthead.start() #inicia a thread
