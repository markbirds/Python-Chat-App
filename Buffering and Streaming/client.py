import socket

HEADERSIZE = 10

client = socket.socket()
client.connect((socket.gethostname(), 9999))

full_message = ''
new_message = True
while True:
	message = client.recv(8) #receiving 8 bytes , 1 char == 1 byte

	if new_message:
		print(f'\nNew message length: {message[:HEADERSIZE]}') #printing the length of message in byte
		message_length = int(message[:HEADERSIZE]) #converting the length in bytes into int
		new_message = False

	full_message += message.decode("utf-8")

	if len(full_message) - HEADERSIZE == message_length: #checks if all parts the message is sent
		print('Full message received.')
		print(full_message[HEADERSIZE:])
		new_message = True
		full_message = ''
