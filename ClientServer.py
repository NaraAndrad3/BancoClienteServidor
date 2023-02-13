import socket
import server


class ClientServer():
    def __init__(self,ip,door):
        self.ip = ip
        self.door = door
        self.add = ((self.ip,self.door))
        print('add: ',self.add)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.add) #realiza a conexão
    
    def send(self,solicitacao):
        self.client_socket.send(solicitacao.encode())
        
    def recebe(self,tam):
        print('Ate aqui ta indo')
        recebe = self.client_socket.recv(tam).decode()
        recebe = recebe.split('*')
        return recebe
        