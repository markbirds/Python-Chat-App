import socket
import time

HEADERSIZE = 10

server = socket.socket()
server.bind((socket.gethostbyname(socket.gethostname()), 9999)) # ip address/server , port number, can be localhost
server.listen(2) # maximum of two clients on queue
print('Server: ',socket.gethostbyname(socket.gethostname()))

while True:
    print('Waiting for a connection...')
    connection, address = server.accept() #waits for connection
    print(f'Connection from {address} has been established!')
    print(connection)

    message = 'Welcome to the server!'
    message = f'{len(message):<{HEADERSIZE}}' + message #sending length of message with 10 extra whitespaces and message
    print('\nSending this message:\n',message)

    connection.send(bytes(message, 'utf-8'))

    while True:
        message = connection.recv(1024).decode("utf-8")
        print('\nServer received this message:',message)
        print('Will echo this message back to client')
        message = f'{len(message):<{HEADERSIZE}}' + message
        connection.send(bytes(message, 'utf-8'))


