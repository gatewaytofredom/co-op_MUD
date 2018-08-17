
class Client:

    def connect_to_server(self,ip,port,username,password):
        pass

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
        except:
            print('sucks to suck, server responses dont exist')

    


if __name__ == "__main__":
    client = Client()

    pre_connection(client)

    client.main_loop()

        
