import threading
import socket
from datetime import datetime
import sys

host = '127.0.0.1'
port = 8000
today = datetime.today()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)
    
def handle(client):
    while True:
        try: 
            message = client.recv(1024)
            broadcast(message)
        except:
            
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            now = datetime.now()
            time = datetime.strftime(now, '%H:%M')
            try:
                nicknames.remove[nickname]
            except:
                print(f"{nickname} left the chat.")
                broadcast(f"---- {nickname} left the chat ----". encode('ascii'))
                if(len(clients) == 1):
                    broadcast(f'\n({time}) Broadcast : You are alone here.'. encode('ascii'))
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        currentDate = today.strftime("%d/%m/%Y")
        print(f'Nickname of the client is {nickname}.')
        client.send(f"Connected to the server\n{currentDate}\n". encode('ascii'))
        broadcast(f'---- {nickname} has joined the chat ----'. encode('ascii'))
        if(len(clients) == 1):
            now = datetime.now()
            time = datetime.strftime(now, '%H:%M')
            broadcast(f'\n({time}) Broadcast : You are alone here.'. encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
print("Server is Online!")       
receive()