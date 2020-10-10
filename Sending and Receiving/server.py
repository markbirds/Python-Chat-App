import socket

server = socket.socket()
server.bind((socket.gethostname(), 9999)) # ip address/server , port number
server.listen(3) # maximum of three clients on queue
print('Server: ',socket.gethostname())

while True:
	print('Waiting for a connection...')
	connection, address = server.accept() #waits for connection
	print(f'Connection from {address} has been established!')
	connection.send(bytes('Welcome to the server!', 'utf-8'))
	connection.close()
