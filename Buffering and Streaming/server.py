import socket
import time

HEADERSIZE = 10

server = socket.socket()
server.bind((socket.gethostname(), 9999)) # ip address/server , port number, can be localhost
server.listen(2) # maximum of two clients on queue
print('Server: ',socket.gethostname())

while True:
	print('Waiting for a connection...')
	connection, address = server.accept() #waits for connection
	print(f'Connection from {address} has been established!')

	message = 'Welcome to the server!'
	message = f'{len(message):<{HEADERSIZE}}' + message #sending length of message with 10 extra whitespaces and message
	print('\nSending this message:\n',message)

	connection.send(bytes(message, 'utf-8'))

	while True:
		# time.sleep(3)
		# message =f'The time is {time.time()}'
		# message = f'{len(message):<{HEADERSIZE}}' + message
		# print('Sending this message:\n',message)
		# client.send(bytes(message, 'utf-8'))
		message = input('\nSend message to client: ')
		print('\nSending this message:\n',message)
		message = f'{len(message):<{HEADERSIZE}}' + message
		connection.send(bytes(message, 'utf-8'))


