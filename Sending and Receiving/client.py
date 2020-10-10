import socket

client = socket.socket()
client.connect((socket.gethostname(), 9999))

full_message = ''

while True:
	message = client.recv(8)
	if len(message) <= 0:
		break
	full_message += message.decode("utf-8")

print(full_message)