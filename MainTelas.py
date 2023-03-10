from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import sys
import random
from ClientServer import *

from TelaInicial import *
from TelaCadastro import *
from TelaDepositar import *
from TelaLogin import *
from TelaTransferir import *
from TelaExtrato import *
from TelaHistorico import *
from TelaSacar import *
from Banco import *
from Conta import *
import socket
cpfAtual = ''

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)

        #A Quantidade de stacks é a quantidade de telas
        #tem que fazer um para cada
        self.Qtstack = QtWidgets.QStackedLayout()
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        #Cria obejtos das telas e "Empilha elas"
        self.tela_inicial = TelaInicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastrar = TelaCadastrar()
        self.tela_cadastrar.setupUi(self.stack1)

        self.tela_login = TelaLogin()
        self.tela_login.setupUi(self.stack2)

        self.tela_depositar = TelaDepositar()
        self.tela_depositar.setupUi(self.stack3)

        self.tela_sacar = TelaSacar()
        self.tela_sacar.setupUi(self.stack4)

        self.tela_transferir = TelaTransferir()
        self.tela_transferir.setupUi(self.stack5)

        self.tela_extrato = TelaExtrato()
        self.tela_extrato.setupUi(self.stack6)

        self.tela_historico = TelaHistorico()
        self.tela_historico.setupUi(self.stack7)

        self.Qtstack.addWidget(self.stack0)
        self.Qtstack.addWidget(self.stack1)
        self.Qtstack.addWidget(self.stack2)
        self.Qtstack.addWidget(self.stack3)
        self.Qtstack.addWidget(self.stack4)
        self.Qtstack.addWidget(self.stack5)
        self.Qtstack.addWidget(self.stack6)
        self.Qtstack.addWidget(self.stack7)

        
    def AbrirTelaInicial(self):
        self.Qtstack.setCurrentIndex(0)

    def AbrirTelaCadastrar(self):
        self.Qtstack.setCurrentIndex(1)
    
    def AbrirTelaLogin(self):
        self.Qtstack.setCurrentIndex(2)
    
    def AbrirTelaDepositar(self):
        self.Qtstack.setCurrentIndex(3)
    
    def AbrirTelaSacar(self):
        self.Qtstack.setCurrentIndex(4)
    
    def AbrirTelaTransferir(self):
        self.Qtstack.setCurrentIndex(5)
    
        
class Main(QMainWindow,Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        #Cria um objeto cliente-servidor
        #######################################################
        self.server = ClientServer('10.180.45.43',9068)
         ########################################################

        self.banco = BancoGeral()

        #Tela Inicial
        self.tela_inicial.pushButton_2.clicked.connect(self.AbrirTelaCadastrar)
        self.tela_inicial.pushButton.clicked.connect(self.botaoLogin)

        #Tela cadastrar
        self.tela_cadastrar.pushButton.clicked.connect(self.botaoCadastrar)
        self.tela_cadastrar.pushButton_2.clicked.connect(self.AbrirTelaInicial)

        #Tela de Login
        self.tela_login.pushButton_5.clicked.connect(self.AbrirTelaInicial)
        self.tela_login.pushButton_2.clicked.connect(self.AbrirTelaDepositar)
        self.tela_login.pushButton.clicked.connect(self.AbrirTelaSacar)
        self.tela_login.pushButton_3.clicked.connect(self.AbrirTelaTransferir)
        self.tela_login.pushButton_4.clicked.connect(self.AbrirTelaExtrato)
        self.tela_login.pushButton_6.clicked.connect(self.AbrirTelaHistorico)

        #Tela Depositar
        self.tela_depositar.pushButton.clicked.connect(self.AbrirTelaDepositar)
        self.tela_depositar.pushButton_2.clicked.connect(self.AbrirTelaLogin)
        self.tela_depositar.pushButton.clicked.connect(self.botaoConfirmarDeposito)

        #Tela Sacar
        self.tela_sacar.pushButton.clicked.connect(self.botaoConfirmarSaque)
        self.tela_sacar.pushButton_2.clicked.connect(self.AbrirTelaLogin)

        #Tela Transferir
        self.tela_transferir.pushButton.clicked.connect(self.botaoConfirmarTransferencia)
        self.tela_transferir.pushButton_2.clicked.connect(self.AbrirTelaLogin)

        #Tela Extrato
        self.tela_extrato.pushButton.clicked.connect(self.AbrirTelaLogin)

        #Tela Historico
        self.tela_historico.pushButton.clicked.connect(self.AbrirTelaLogin)

    #Envia a operação a ser realizada para o servidor
    def serverSolicit(self,solicitacao):
        self.server.send(solicitacao)
        recv = self.server.recebe(2048)
        print('print 1',recv)
       # decodifica = recv.decode().split('*') #decodifica o retorno do servidor
        return recv

    def botaoLogin(self):
        op = '01' #Operação de login
        cpf = self.tela_inicial.lineEdit_2.text()
        senha = self.tela_inicial.lineEdit.text()
        solicitacao = f'{op}*{cpf}*{senha}'
        retornoServer = self.serverSolicit(solicitacao) #mandei para o servidor
        print('retorno do servidor',retornoServer)
        print('ja chegou do servidor')
        if ( retornoServer[0] == 'True'):
            self.tela_inicial.lineEdit_2.setText('')
            self.tela_inicial.lineEdit.setText('')
            global cpfAtual #declarando a variavel como global
            cpfAtual = cpf
            QMessageBox.information(None,'Atenção','Login Realizado com sucesso')
            self.AbrirTelaLogin()
            self.tela_login.label_8.setText(str(retornoServer[1]))
            self.tela_login.label_5.setText(str(retornoServer[2]))
            self.tela_login.label_6.setText(str(retornoServer[3]))
        else:
            QMessageBox.information(None,'Atenção','Usuário não encontrado')
    #Falta arrumar essa parte da transferencia
    def botaoConfirmarTransferencia(self):
        op = '05'
        valor = self.tela_transferir.lineEdit_2.text()
        valor = float(valor)
        destino = self.tela_transferir.lineEdit.text()
        senha = self.tela_transferir.lineEdit_4.text()
        solicitacao = f'{op}*{cpfAtual}*{destino}*{valor}*{senha}'
        retornoServer = self.serverSolicit(solicitacao)

        if(retornoServer[0] == 'True'):
            QMessageBox.information(None,'Atenção','Transferencia realizada com sucesso')
            self.tela_transferir.lineEdit_2.setText('')
            self.tela_transferir.lineEdit.setText('')
            self.tela_transferir.lineEdit_4.setText('')
        else:
            QMessageBox.information(None,'Atenção','Não foi possivel realizar a operação')
            self.tela_transferir.lineEdit_4.setText('')

    def botaoConfirmarSaque(self):
        valor = self.tela_sacar.lineEdit_2.text()
        senha = self.tela_sacar.lineEdit_3.text()
        op = '04'
        solicitacao = f'{op}*{cpfAtual}*{valor}*{senha}'
        retorno = self.serverSolicit(solicitacao)
        if (retorno[0] == 'True'):
            QMessageBox.information(None,'Atenção','Saque Realizado com sucesso')
            self.tela_sacar.lineEdit_2.setText('')
            self.tela_sacar.lineEdit_3.setText('')
        else:
            QMessageBox.information(None,'Atenção','A Operação não pôde ser concluída')   
            self.tela_sacar.lineEdit_2.setText('')
            self.tela_sacar.lineEdit_3.setText('') 
    
    def botaoConfirmarDeposito(self):
        valor = self.tela_depositar.lineEdit.text()
        valor = float(valor)
        op = '03' #define o ID da operação
        solicitacao = f'{op}*{cpfAtual}*{valor}'
        retorno = self.serverSolicit(solicitacao)
        if(retorno[0] == 'True'):
            QMessageBox.information(None,'Atenção','Depósito Realizado com sucesso')
            self.tela_depositar.lineEdit.setText('') 
        else:
            QMessageBox.information(None,'Atenção','A Operação não pôde ser concluída')    
            self.tela_depositar.lineEdit.setText('')
            
    
    def AbrirTelaExtrato(self):
        op = '06' #Operação de Extrato
        solicitacao = f'{op}*{cpfAtual}'
        retornoServer = self.serverSolicit(solicitacao)
        extrato = ''
        if(retornoServer[0] == 'True'):
            QMessageBox.information(None,'Atenção','Extrato gerado com sucesso')
            self.Qtstack.setCurrentIndex(6)
            extrato ='\tEXTRATO\n\n-------------------------------------\n-- Nome: ' + str(retornoServer[1]) + '\n' + '-- Numero: ' + str(retornoServer[2]) + '\n' + '-- Saldo: R$ ' + str(retornoServer[3]) + '\n-------------------------------------'
            self.tela_extrato.textEdit.setText(str(extrato))
        else:
            QMessageBox.information(None,'Atenção','Não foi possivel realizar esta operação')

    def AbrirTelaHistorico(self):
        op = '07'
        solicitacao = f'{op}*{cpfAtual}'
        retornoServer = self.serverSolicit(solicitacao)
        if retornoServer[0] == 'True':
            self.Qtstack.setCurrentIndex(7)
            QMessageBox.information(None,'Atenção','Histórico gerado com sucesso')
            self.tela_historico.textEdit.setText(retornoServer[1])

    def botaoCadastrar(self):
        nome = self.tela_cadastrar.lineEdit.text()
        cpf = self.tela_cadastrar.lineEdit_2.text()
        nascimento = self.tela_cadastrar.lineEdit_5.text()
        senha = self.tela_cadastrar.lineEdit_3.text()
        confirmSenha = self.tela_cadastrar.lineEdit_4.text()
        if (senha == confirmSenha):
            if not(nome == '' or cpf == '' or senha == ''):
                op = '02'
                p = Pessoa(nome,cpf,nascimento)
                #self.banco.add_pessoa(p)
                numero = random.randint(100,999)
                numero = str(numero)
                conta = Conta(p,numero,senha)
                solicitacao = f'{op}*{nome}*{cpf}*{nascimento}*{senha}*{numero}'
                retornoServer = self.serverSolicit(solicitacao)
                    #self.banco.add_conta(conta,cpf)
                if retornoServer[0] == 'True':
                    QMessageBox.information(None,'Atenção','Cadastro Realizado com sucesso')
                    self.tela_cadastrar.lineEdit.setText('')
                    self.tela_cadastrar.lineEdit_2.setText('')
                    self.tela_cadastrar.lineEdit_5.setText('')
                    self.tela_cadastrar.lineEdit_3.setText('')
                    self.tela_cadastrar.lineEdit_4.setText('')
                else:
                    QMessageBox.information(None,'Atenção','Operação não concluida')
            else:
                QMessageBox.information(None,'Atenção','Todos os campos devem ser preenchidos')
        else:
            QMessageBox.information(None,'Atenção','As senhas não conferem')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())