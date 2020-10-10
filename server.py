import socket
import threading

HEADERSIZE = 10
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDRESS = (SERVER,PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS) #bind address to server
server.listen() 
print('Server: ',SERVER)

client_list = []

# sends user disconnection to all users in server
def disconnect_message(client,username):
    message = f'{username} left the server.' 
    for connection in client_list:
        if connection != client:
            broadcast_message = f'{len(message):<{HEADERSIZE}}' + message
            connection.send(broadcast_message.encode(FORMAT))

def handle_client(client, address):
    connected = True
    client_list.append(client)
    print(f'Connection from {address} has been established!')

    username_length = client.recv(HEADERSIZE).decode(FORMAT)
    if username_length:
        username_length = int(username_length)
        username = client.recv(username_length).decode(FORMAT)

    while connected:
        try:
            message_length = client.recv(HEADERSIZE).decode(FORMAT)
            if message_length:
                message_received = client.recv(int(message_length)).decode(FORMAT)
                message = f'{username}: {message_received}'
                # broadcasts the message to all clients in the server 
                for connection in client_list:
                    if connection != client:
                        broadcast_message = f'{len(message):<{HEADERSIZE}}' + message
                        connection.send(broadcast_message.encode(FORMAT))

                if message_received == 'DISCONNECT':
                    connected = False
                    disconnect_message(client,username)
                    client_list.remove(client)
                    
        except:
            connected = False
            disconnect_message(client,username)
            client_list.remove(client)
    print(f'{username} disconnected.')
    client.close()
        

def start():
    while True:
        print('Waiting for a client...')
        client, address = server.accept() #waits for client/ blocking code
        # multi threading to handle multiple threads of users while waiting for another connection
        thread = threading.Thread(target=handle_client,args=(client, address))
        thread.start()
        client_count = f'Number of users in the server: {threading.activeCount() - 1}'
        client_count = f'{len(client_count):<{HEADERSIZE}}' + client_count
        client.send(client_count.encode(FORMAT))


start()
