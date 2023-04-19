import socket
import threading
import random

HOST = 'localhost'
PORT = 5000
button_x = random.randint(0, 690)
button_y = random.randint(0, 490)
score = 1


def handle_client(connection, address):
    global button_x, button_y, score
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        if data == 'send':
            response = f'{button_x},{button_y},{score}'
            connection.send(response.encode())
        elif data == 'got it':
            button_x = random.randint(0, 690)
            button_y = random.randint(0, 490)
            score += 1
    print(f'Client from {address} disconnected')
    connection.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
