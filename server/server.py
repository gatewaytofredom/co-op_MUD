import sys
import socket
from threading import Thread

class Server():

    def __init__(self,port):
        self.port = port
        self.host = socket.gethostbyname(socket.gethostname())
        print(self.host)

        if self.port == '':
            self.port = 6624

        try:
            self.s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((self.host,self.port))

            #change to number of players + 1
            self.s.listen(10)
            print('Server bind to port sucsesful')

        except:
            print('unable to start server. possible port conflict')


    def verify_client(self,username,password):
        #Sqlite database probs
        pass

    def create_conection_thread(self):
        t = Thread(target= self.wait_for_connection)
        t.daemon = True
        t.start()

    def wait_for_connection(self):
        while True:
            con = clientsocket,addr = self.s.accept()
            t = Thread(target=self.client_connection(self,con))
            t.daemon = True
            t.start()



    def client_connection(self, clientsocket, addr):
        #make not while true
        while True:
            clientsocket.send("AAA".encode())
            clientsocket.recv(1024).decode()


server = Server(port=6624)

server.wait_for_connection()





        
        




    