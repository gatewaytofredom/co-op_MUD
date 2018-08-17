import sys
import socket
from threading import Thread

class Server():

    def __init__(self,port):
        self.port = port
        self.host = socket.gethostbyname()
        print(self.host)

        try:
            self.s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            self.s.bind((self.host,self.port))

            #change to number of players + 1
            self.s.listen(10)
        except:
            print('unable to start server. possible port conflict')


    def verify_client(self,username,password):
        #Sqlite database probs
        pass

    def conenction_listener(self):

        t = Thread(target= self.listener_loop)
        t.daemon = True
        t.start()

    def listener_loop(self):
        while True:
           con = clientsocket,addr = self.s.accept()


    def handle_client(self, clientsocket, addr):
        #make not while true
        while True:
           clientsocket.send("AAA".encode())
           clientsocket.recv(1024).decode()

        




    


if __name__ == "__main__":
    server = Server(sys.argv[1])




    