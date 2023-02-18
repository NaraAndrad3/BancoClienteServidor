import socket
import server


class ClientServer():
    """
        classe clienteserver coneceta o servidor com o cliente

        Attributes
        ----------
            ip: str
                recebe o ip fornececido pelo serivdor
            doar: str
                host em que o serivodor esta ospedado
        
        Methods
        -------
            send(solicitacao: str)
                envia mensagem ao servidor
            
            recebe(tam: int)
                recebe a mensagem eviada do servidor

    """
    def __init__(self,ip,door):
        self.ip = ip
        self.door = door
        self.add = ((self.ip,self.door))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.add) #realiza a conexão
    
    def send(self,solicitacao):
        """
            Função que envia solicitação para o serividor

            Parameteres
            -----------
            solicitacao: str
                mensagem informando a solicitação para o servidor
            
            Returns:
            --------
                None
                
        """
        self.client_socket.send(solicitacao.encode())
        
    def recebe(self,tam):
        """
            Função que recebe a mensagem do servidor

            Parameteres
            -----------
            tam: int
                tamanho em bytes das mensagem recebida
               
            
            Returns
            -------
            recebe: str
                retorna a string recebida na mensagem

                
        """
        recebe = self.client_socket.recv(tam).decode()
        recebe = recebe.split('*')
        return recebe
        