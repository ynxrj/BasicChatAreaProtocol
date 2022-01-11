import socket
import threading
from datetime import datetime
import os 

command = 'clear'
if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
os.system(command)


nickname = input("Set your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if(message == 'NICK'):
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception as e:
            print("An error occurred!", e)
            client.close()
            break

def write():
    while True:
        now = datetime.now()
        time = datetime.strftime(now, '%H:%M')
        message = f'({time}) {nickname} : {input("")}'
        client.send(f"{message}".encode('ascii'))
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()