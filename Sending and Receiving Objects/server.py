import socket
import pickle

HEADERSIZE = 10

server = socket.socket()
server.bind((socket.gethostname(), 9999)) # ip address/server , port number, can be localhost
server.listen(2) # maximum of two clients on queue
print('Server: ',socket.gethostname())

while True:
    print('Waiting for a connection...')
    connection, address = server.accept() #waits for connection
    print(f'Connection from {address} has been established!')



    obj = {1:"Hey!",2:"There"}
    message = pickle.dumps(obj)
    message = bytes(f'{len(message):<{HEADERSIZE}}', 'utf-8') + message 

    connection.send(message)
