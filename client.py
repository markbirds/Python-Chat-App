import socket
import threading

HEADERSIZE = 10
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9999
ADDRESS = (SERVER,PORT)
FORMAT = 'utf-8'

username = input('Enter your username: ')
username = f'{len(username):<{HEADERSIZE}}' + username

client = socket.socket()
client.connect(ADDRESS)
client.send(username.encode(FORMAT))

def receive_message():
    while True:
        message_length = client.recv(HEADERSIZE).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            print(client.recv(message_length).decode(FORMAT))

thread = threading.Thread(target=receive_message)
thread.start()

print('\nType your message and hit ENTER...')    
print('Type DISCONNECT to disconnect...\n')    
while True:
    message = input('')
    message = f'{len(message):<{HEADERSIZE}}' + message
    client.send(message.encode(FORMAT))