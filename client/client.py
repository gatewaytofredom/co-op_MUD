import socket
class Client:

    def connect_to_server(self,ip,port,username,password):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (ip,port)
        print('connecting to {} port {}'.format(*self.server_address))
        self.sock.connect(self.server_address)
        self.sock.send("gucci".encode())

    def send(self,data):
        pass

    def recieve(self):
        pass

    def get_input(self):
        pass

    def main_loop(self):
        pass

    

def pre_connection(client):
    server_connected = False

    while not server_connected:

        ip = input('Enter the server IP address: ')
        port = input('Enter the server port (default 6624): ')
        usr = input('Enter your username: ')
        password = input('Enter your password: ')

        if port == '':
            port = 6624

        try:
            client.connect_to_server(ip,port,usr,password)
            server_connected = True
        except Exception as e:
            print(e)
    


if __name__ == "__main__":
    client = Client()

    pre_connection(client)

    client.main_loop()

        
